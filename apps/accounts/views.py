from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import CustomUser


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard:index')

    next_url = request.GET.get('next') or request.POST.get('next') or ''

    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()

        if not email or not password:
            messages.error(request, 'Please provide both email and password.')
        else:
            user = authenticate(request, username=email, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, f'Welcome back, {user.first_name or user.email}!')
                if next_url:
                    return redirect(next_url)
                return redirect('dashboard:index')
            else:
                messages.error(request, 'Invalid email or password. Please try again.')

    context = {
        'next': next_url,
    }
    return render(request, 'users/login.html', context)


def logout_view(request):
    auth_logout(request)
    messages.info(request, 'You have been logged out successfully.')
    return redirect('landing_page')


def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard:index')

    if request.method == 'POST':
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        company_name = request.POST.get('company_name', '').strip()
        password = request.POST.get('password', '').strip()
        confirm_password = request.POST.get('confirm_password', '').strip()

        if not email or not password:
            messages.error(request, 'Email and password are required.')
        elif password != confirm_password:
            messages.error(request, 'Passwords do not match.')
        elif CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'An account with this email already exists.')
        else:
            user = CustomUser.objects.create_user(
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                company_name=company_name,
                role=CustomUser.Role.COMPANY,
                status=CustomUser.Status.VERIFIED
            )
            auth_login(request, user)
            messages.success(request, 'Account created successfully! Please select your subscription plan.')
            return redirect('billing:purchase')

    return render(request, 'users/register.html')


def users_list(request):
    query = request.GET.get('q', '').strip()
    role_filter = request.GET.get('role', '').strip()

    users = CustomUser.objects.all().order_by('-date_joined')
    if query:
        users = users.filter(
            Q(email__icontains=query) |
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(company_name__icontains=query) |
            Q(phone__icontains=query)
        )
    if role_filter:
        users = users.filter(role=role_filter)

    total_count = CustomUser.objects.count()
    superadmin_count = CustomUser.objects.filter(role=CustomUser.Role.SUPERADMIN).count()
    company_count = CustomUser.objects.filter(role__in=[CustomUser.Role.ADMIN, CustomUser.Role.COMPANY]).count()
    driver_count = CustomUser.objects.filter(role=CustomUser.Role.DRIVER).count()

    context = {
        'users': users,
        'query': query,
        'role_filter': role_filter,
        'total_count': total_count,
        'superadmin_count': superadmin_count,
        'company_count': company_count,
        'driver_count': driver_count,
        'role_choices': CustomUser.Role.choices,
        'current_dashboard': 'superadmin' if request.user.is_superuser or getattr(request.user, 'role', '') == 'superadmin' else 'admin',
    }
    return render(request, 'users/list.html', context)

