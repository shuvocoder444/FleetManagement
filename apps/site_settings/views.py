from django.shortcuts import render, redirect
from django.contrib import messages
from .models import WebsiteSetting, Currency, ContactMessage
from apps.billing.models import Plan


def landing_page(request):
    setting = WebsiteSetting.load()
    plans = Plan.objects.filter(status=Plan.Status.ACTIVE).order_by('price')
    currencies = Currency.objects.filter(is_active=True)
    
    # Handle Contact Form submission
    if request.method == 'POST' and 'contact_submit' in request.POST:
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        message_text = request.POST.get('message', '').strip()
        
        if name and email and message_text:
            ContactMessage.objects.create(
                name=name,
                email=email,
                phone=phone,
                message=message_text
            )
            messages.success(request, 'Your message has been sent successfully! Our team will contact you soon.')
            return redirect('landing_page')
        else:
            messages.error(request, 'Please fill in all required fields.')

    context = {
        'setting': setting,
        'plans': plans,
        'currencies': currencies,
    }
    return render(request, 'landing/index.html', context)


def switch_currency(request, code):
    if Currency.objects.filter(code=code, is_active=True).exists():
        request.session['currency'] = code
    next_url = request.META.get('HTTP_REFERER', '/')
    return redirect(next_url)


def switch_language(request, lang_code):
    if lang_code in ['en', 'ru']:
        request.session['_language'] = lang_code
        request.session['django_language'] = lang_code
    next_url = request.META.get('HTTP_REFERER', '/')
    response = redirect(next_url)
    response.set_cookie('django_language', lang_code, max_age=365*24*3600, path='/')
    return response


def settings_view(request):
    setting = WebsiteSetting.load()

    if request.method == 'POST':
        setting.site_name = request.POST.get('site_name', 'Topd').strip()
        setting.contact_email = request.POST.get('contact_email', '').strip()
        setting.contact_phone = request.POST.get('contact_phone', '').strip()
        setting.address = request.POST.get('address', '').strip()
        setting.working_hours = request.POST.get('working_hours', '').strip()
        setting.facebook_url = request.POST.get('facebook_url', '').strip()
        setting.twitter_url = request.POST.get('twitter_url', '').strip()
        setting.instagram_url = request.POST.get('instagram_url', '').strip()
        setting.linkedin_url = request.POST.get('linkedin_url', '').strip()

        if request.FILES.get('logo'):
            setting.logo = request.FILES.get('logo')

        setting.save()
        messages.success(request, 'Website settings saved successfully!')
        return redirect('site_settings:settings')

    context = {
        'setting': setting,
        'current_dashboard': 'superadmin' if request.user.is_superuser or getattr(request.user, 'role', '') == 'superadmin' else 'admin',
    }
    return render(request, 'settings/general.html', context)
