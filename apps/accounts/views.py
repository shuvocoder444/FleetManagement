from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import CustomUser


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
