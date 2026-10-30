import os, sys
sys.path.insert(0, r'D:\new')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import django
django.setup()

from apps.accounts.models import CustomUser, ActivityLog
from django.utils import timezone
import datetime

# Find or get company owner Bakyt
company = CustomUser.objects.filter(email='bakyt@bishkekwheels.kg').first()
if not company:
    company = CustomUser.objects.filter(role=CustomUser.Role.COMPANY).first()

if company:
    company.member_role = 'Owner'
    company.save()
    print('Company:', company.email)

    # 1. Create 1 Team Member (e.g. Almaz Asanov - Manager)
    almaz_email = 'almaz.manager@bishkekwheels.kg'
    member, created = CustomUser.objects.get_or_create(
        email=almaz_email,
        defaults={
            'first_name': 'Almaz',
            'last_name': 'Asanov',
            'phone': '+996 555 889900',
            'role': CustomUser.Role.COMPANY,
            'company': company,
            'member_role': 'Manager',
            'status': CustomUser.Status.VERIFIED
        }
    )
    if created:
        member.set_password('Manager123!')
        member.save()
        print('Created sample member:', member.email)
    else:
        print('Sample member already exists:', member.email)

    # 2. Seed realistic activity logs
    now = timezone.now()
    sample_logs = [
        (
            company,
            company.get_full_name() or "Bakyt",
            company.email,
            "Owner",
            ActivityLog.ActionType.CREATE,
            ActivityLog.Module.TEAM,
            "Added new team member Almaz Asanov (almaz.manager@bishkekwheels.kg) as Manager (Seat 2 of 3)",
            now - datetime.timedelta(hours=5)
        ),
        (
            member,
            "Almaz Asanov",
            member.email,
            "Manager",
            ActivityLog.ActionType.LOGIN,
            ActivityLog.Module.AUTH,
            "Manager logged into company portal",
            now - datetime.timedelta(hours=4, minutes=30)
        ),
        (
            member,
            "Almaz Asanov",
            member.email,
            "Manager",
            ActivityLog.ActionType.VERIFY,
            ActivityLog.Module.DRIVERS,
            "Ran anti-fraud driver background verification search for query: 'ID3876029' - Status: Clean background",
            now - datetime.timedelta(hours=3, minutes=15)
        ),
        (
            member,
            "Almaz Asanov",
            member.email,
            "Manager",
            ActivityLog.ActionType.CREATE,
            ActivityLog.Module.AGREEMENTS,
            "Created rental agreement #AGR-2026-003 for client Rustam K. (Vehicle: Toyota Camry, 01KG777ABC)",
            now - datetime.timedelta(hours=2, minutes=45)
        ),
        (
            company,
            company.get_full_name() or "Bakyt",
            company.email,
            "Owner",
            ActivityLog.ActionType.CREATE,
            ActivityLog.Module.VEHICLES,
            "Added vehicle 'Hyundai Sonata 2022' (01KG888XYZ) to fleet garage",
            now - datetime.timedelta(hours=1, minutes=10)
        ),
        (
            member,
            "Almaz Asanov",
            member.email,
            "Manager",
            ActivityLog.ActionType.UPDATE,
            ActivityLog.Module.AGREEMENTS,
            "Updated contract deposit status to confirmed ($2,465.00) for agreement #AGR-2026-003",
            now - datetime.timedelta(minutes=25)
        ),
    ]

    for actor, name, email, role, act_type, module, desc, dt in sample_logs:
        log, c = ActivityLog.objects.get_or_create(
            company=company,
            description=desc,
            defaults={
                'actor': actor,
                'actor_name': name,
                'actor_email': email,
                'actor_role': role,
                'action_type': act_type,
                'module': module,
                'ip_address': '195.250.26.201',
            }
        )
        if c:
            # Manually set created_at timestamp
            ActivityLog.objects.filter(id=log.id).update(created_at=dt)

    print('Seeded activity logs count:', ActivityLog.objects.filter(company=company).count())
    print('Current seats used:', company.team_seat_count, '/', company.max_allowed_seats)

