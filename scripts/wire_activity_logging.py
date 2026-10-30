# 1. Update apps/agreements/views.py
with open(r'D:\new\apps\agreements\views.py', 'r', encoding='utf-8') as f:
    c = f.read().replace('\r\n', '\n')

c = c.replace(
    "from apps.site_settings.context_processors import get_active_dashboard_role\nfrom django.shortcuts import render",
    "from apps.site_settings.context_processors import get_active_dashboard_role\nfrom apps.accounts.utils import log_activity\nfrom apps.accounts.models import ActivityLog\nfrom django.shortcuts import render"
)

log_stmt = """            messages.success(request, f'Agreement {agreement.contract_number} created successfully!')
            log_activity(
                request,
                ActivityLog.ActionType.CREATE,
                ActivityLog.Module.AGREEMENTS,
                f"Created rental agreement #{agreement.contract_number} for client {agreement.client_name} (Vehicle: {vehicle.title})"
            )"""

c = c.replace(
    "messages.success(request, f'Agreement {agreement.contract_number} created successfully!')",
    log_stmt
)

with open(r'D:\new\apps\agreements\views.py', 'w', encoding='utf-8') as f:
    f.write(c)
print("Updated agreements views")

# 2. Update apps/vehicles/views.py
with open(r'D:\new\apps\vehicles\views.py', 'r', encoding='utf-8') as f:
    c = f.read().replace('\r\n', '\n')

c = c.replace(
    "from apps.site_settings.context_processors import get_active_dashboard_role\nfrom django.shortcuts import render",
    "from apps.site_settings.context_processors import get_active_dashboard_role\nfrom apps.accounts.utils import log_activity\nfrom apps.accounts.models import ActivityLog\nfrom django.shortcuts import render"
)

log_stmt_v = """            messages.success(request, f'Vehicle "{vehicle.title}" added to garage successfully!')
            log_activity(
                request,
                ActivityLog.ActionType.CREATE,
                ActivityLog.Module.VEHICLES,
                f"Added vehicle '{vehicle.title}' ({vehicle.registration_number}) to fleet garage"
            )"""

c = c.replace(
    'messages.success(request, f\'Vehicle "{vehicle.title}" added to garage successfully!\')',
    log_stmt_v
)

with open(r'D:\new\apps\vehicles\views.py', 'w', encoding='utf-8') as f:
    f.write(c)
print("Updated vehicles views")

# 3. Update apps/drivers/views.py
with open(r'D:\new\apps\drivers\views.py', 'r', encoding='utf-8') as f:
    c = f.read().replace('\r\n', '\n')

c = c.replace(
    "from apps.site_settings.context_processors import get_active_dashboard_role\nfrom django.shortcuts import render",
    "from apps.site_settings.context_processors import get_active_dashboard_role\nfrom apps.accounts.utils import log_activity\nfrom apps.accounts.models import ActivityLog\nfrom django.shortcuts import render"
)

log_stmt_d = """        driver = Driver.objects.create(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            passport_number=passport_number,
            license_number=license_number,
            personal_id=personal_id,
            rating_status=rating_status,
            average_rating=float(average_rating) if average_rating else 5.0,
            status=status,
            notes=notes,
            avatar=avatar
        )
        log_activity(
            request,
            ActivityLog.ActionType.CREATE,
            ActivityLog.Module.DRIVERS,
            f"Added new agency driver {driver.first_name} {driver.last_name} ({driver.license_number})"
        )"""

c = c.replace(
    """        driver = Driver.objects.create(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            passport_number=passport_number,
            license_number=license_number,
            personal_id=personal_id,
            rating_status=rating_status,
            average_rating=float(average_rating) if average_rating else 5.0,
            status=status,
            notes=notes,
            avatar=avatar
        )""",
    log_stmt_d
)

log_stmt_chk = """        if query:
            drivers = drivers.filter(
                models.Q(first_name__icontains=query) |
                models.Q(last_name__icontains=query) |
                models.Q(passport_number__icontains=query) |
                models.Q(license_number__icontains=query) |
                models.Q(personal_id__icontains=query)
            )
            log_activity(
                request,
                ActivityLog.ActionType.VERIFY,
                ActivityLog.Module.DRIVERS,
                f"Ran anti-fraud driver background verification search for query: '{query}'"
            )"""

c = c.replace(
    """        if query:
            drivers = drivers.filter(
                models.Q(first_name__icontains=query) |
                models.Q(last_name__icontains=query) |
                models.Q(passport_number__icontains=query) |
                models.Q(license_number__icontains=query) |
                models.Q(personal_id__icontains=query)
            )""",
    log_stmt_chk
)

with open(r'D:\new\apps\drivers\views.py', 'w', encoding='utf-8') as f:
    f.write(c)
print("Updated drivers views")

