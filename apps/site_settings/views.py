from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.translation import activate
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
        activate(lang_code)
        request.session['django_language'] = lang_code
    next_url = request.META.get('HTTP_REFERER', '/')
    return redirect(next_url)
