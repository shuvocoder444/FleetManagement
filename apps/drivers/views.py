from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Driver, DriverHistory, DriverRating
from apps.accounts.models import CustomUser


def driver_list(request):
    query = request.GET.get('q', '').strip()
    status_filter = request.GET.get('status', '').strip()

    drivers = Driver.objects.all()
    if query:
        drivers = drivers.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(phone__icontains=query) |
            Q(passport_number__icontains=query) |
            Q(license_number__icontains=query) |
            Q(personal_id__icontains=query)
        )
    if status_filter:
        drivers = drivers.filter(status=status_filter)

    total_count = Driver.objects.count()
    available_count = Driver.objects.filter(status=Driver.Status.AVAILABLE).count()
    busy_count = Driver.objects.filter(status=Driver.Status.BUSY).count()
    warning_count = Driver.objects.filter(status=Driver.Status.WARNING).count()

    context = {
        'drivers': drivers,
        'query': query,
        'status_filter': status_filter,
        'total_count': total_count,
        'available_count': available_count,
        'busy_count': busy_count,
        'warning_count': warning_count,
        'current_dashboard': 'superadmin' if request.user.is_superuser or getattr(request.user, 'role', '') == 'superadmin' else 'admin',
    }
    return render(request, 'drivers/list.html', context)


def driver_create(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        phone = request.POST.get('phone', '').strip()
        email = request.POST.get('email', '').strip()
        passport_number = request.POST.get('passport_number', '').strip()
        passport_expiry = request.POST.get('passport_expiry') or None
        license_number = request.POST.get('license_number', '').strip()
        license_expiry = request.POST.get('license_expiry') or None
        personal_id = request.POST.get('personal_id', '').strip()
        status = request.POST.get('status', Driver.Status.AVAILABLE)
        user_comments = request.POST.get('user_comments', '').strip()
        admin_comments = request.POST.get('admin_comments', '').strip()

        if not first_name or not last_name or not passport_number or not personal_id:
            messages.error(request, 'Please fill in all mandatory fields: First Name, Last Name, Passport, and Personal ID.')
        else:
            creator = request.user if request.user.is_authenticated else CustomUser.objects.filter(role='superadmin').first()
            if not creator:
                creator = CustomUser.objects.first()

            driver = Driver.objects.create(
                created_by=creator,
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                email=email,
                passport_number=passport_number,
                passport_expiry=passport_expiry,
                license_number=license_number,
                license_expiry=license_expiry,
                personal_id=personal_id,
                status=status,
                user_comments=user_comments,
                admin_comments=admin_comments
            )
            messages.success(request, f'Driver {driver.full_name} registered successfully!')
            return redirect('drivers:list')

    context = {
        'status_choices': Driver.Status.choices,
        'current_dashboard': 'superadmin' if request.user.is_superuser or getattr(request.user, 'role', '') == 'superadmin' else 'admin',
    }
    return render(request, 'drivers/create.html', context)


def check_driver_view(request):
    query = request.GET.get('q', '').strip()
    passport = request.GET.get('passport', '').strip()
    personal_id = request.GET.get('personal_id', '').strip()

    search_term = query or passport or personal_id
    matched_driver = None
    history_entries = []

    if search_term:
        matched_driver = Driver.objects.filter(
            Q(passport_number__iexact=search_term) |
            Q(personal_id__iexact=search_term) |
            Q(license_number__iexact=search_term)
        ).first()

        if matched_driver:
            history_entries = matched_driver.history_entries.all()

    context = {
        'search_term': search_term,
        'passport': passport,
        'personal_id': personal_id,
        'matched_driver': matched_driver,
        'history_entries': history_entries,
        'current_dashboard': 'superadmin' if request.user.is_superuser or getattr(request.user, 'role', '') == 'superadmin' else 'admin',
    }
    return render(request, 'drivers/check_driver.html', context)


def driver_detail(request, pk):
    driver = get_object_or_404(Driver, pk=pk)
    context = {
        'driver': driver,
        'history_entries': driver.history_entries.all(),
        'ratings': driver.ratings.all(),
        'agreements': driver.agreements.all(),
        'current_dashboard': 'superadmin' if request.user.is_superuser or getattr(request.user, 'role', '') == 'superadmin' else 'admin',
    }
    return render(request, 'drivers/detail.html', context)
