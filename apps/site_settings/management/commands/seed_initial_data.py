from django.core.management.base import BaseCommand
from apps.accounts.models import CustomUser
from apps.site_settings.models import WebsiteSetting, Currency
from apps.billing.models import Plan, Subscription
from apps.vehicles.models import Vehicle
from apps.drivers.models import Driver, DriverHistory, DriverRating
from apps.agreements.models import Agreement
import datetime
from django.utils import timezone


class Command(BaseCommand):
    help = 'Seeds initial settings, currencies, plans, superadmin, admin, and driver'

    def handle(self, *args, **options):
        # 1. Superuser
        superadmin, created = CustomUser.objects.get_or_create(
            email='admin@topd.kg',
            defaults={
                'first_name': 'Super',
                'last_name': 'Admin',
                'phone': '+996 999 083 366',
                'role': CustomUser.Role.SUPERADMIN,
                'status': CustomUser.Status.VERIFIED,
                'company_name': 'Topd HQ',
                'is_staff': True,
                'is_superuser': True,
            }
        )
        if created:
            superadmin.set_password('adminpassword123')
            superadmin.save()
            self.stdout.write(self.style.SUCCESS('Created Super Admin: admin@topd.kg'))

        # 2. Company / Fleet Admin User
        company_user, created = CustomUser.objects.get_or_create(
            email='company@topd.kg',
            defaults={
                'first_name': 'Team',
                'last_name': 'JBDIT',
                'phone': '+8801309126610',
                'role': CustomUser.Role.COMPANY,
                'status': CustomUser.Status.VERIFIED,
                'company_name': 'Team JBDIT Rental Ltd',
                'business_type': 'Car Rental & Fleet Management',
                'is_staff': False,
            }
        )
        if created:
            company_user.set_password('company123')
            company_user.save()
            self.stdout.write(self.style.SUCCESS('Created Fleet Admin: company@topd.kg'))

        # 3. Driver User & Profile
        driver_user, created = CustomUser.objects.get_or_create(
            email='driver@topd.kg',
            defaults={
                'first_name': 'Altynai',
                'last_name': 'Tashmatova',
                'phone': '+996990963030',
                'role': CustomUser.Role.DRIVER,
                'status': CustomUser.Status.VERIFIED,
                'is_staff': False,
            }
        )
        if created:
            driver_user.set_password('driver123')
            driver_user.save()
            self.stdout.write(self.style.SUCCESS('Created Driver User: driver@topd.kg'))

        # Driver Model Record
        driver, _ = Driver.objects.get_or_create(
            passport_number='ID3876029',
            defaults={
                'user': driver_user,
                'created_by': company_user,
                'first_name': 'Altynai',
                'last_name': 'Tashmatova',
                'phone': '+996990963030',
                'email': 'driver@topd.kg',
                'passport_expiry': datetime.date(2034, 4, 11),
                'license_number': 'DL0440211',
                'license_expiry': datetime.date(2028, 10, 22),
                'personal_id': '43333333566342',
                'status': Driver.Status.BUSY,
                'user_comments': 'Experienced driver with clean city driving records.',
                'admin_comments': 'Verified driver. Performance rating 4.8 / 5.0'
            }
        )

        # 4. Vehicles
        v1, _ = Vehicle.objects.get_or_create(
            registration_number='01KG777AAA',
            defaults={
                'created_by': company_user,
                'title': 'Hyundai Sonata 2019',
                'brand': 'Hyundai',
                'model': 'Sonata',
                'year': 2019,
                'color': 'Black',
                'vehicle_type': Vehicle.VehicleType.RENT,
                'status': Vehicle.Status.RENTED,
                'description': 'Comfortable business sedan with heated seats.'
            }
        )
        v2, _ = Vehicle.objects.get_or_create(
            registration_number='01KG888BBB',
            defaults={
                'created_by': company_user,
                'title': 'Honda Accord 2019',
                'brand': 'Honda',
                'model': 'Accord',
                'year': 2019,
                'color': 'White',
                'vehicle_type': Vehicle.VehicleType.RENT,
                'status': Vehicle.Status.AVAILABLE,
                'description': 'Sporty family sedan, low mileage.'
            }
        )

        # 5. Agreement for Driver
        start_t = timezone.now() - datetime.timedelta(days=2)
        end_t = timezone.now() + datetime.timedelta(days=12)
        Agreement.objects.get_or_create(
            contract_number='CONTRACT-2026-0001',
            defaults={
                'created_by': company_user,
                'vehicle': v1,
                'driver': driver,
                'company_name': 'Team JBDIT Rental Ltd',
                'client_name': 'John Doe (Renet Management)',
                'contract_type': Agreement.ContractType.SHORT_TERM,
                'start_date': start_t,
                'end_date': end_t,
                'currency': 'KGS',
                'daily_rental_price': 3400.00,
                'deposit': 25000.00,
                'status': Agreement.Status.ACTIVE,
                'terms_conditions': 'Standard 14-day short-term rental with insurance.'
            }
        )

        # 6. Driver History
        DriverHistory.objects.get_or_create(
            driver=driver,
            history_type=DriverHistory.HistoryType.UNPAID_FINES,
            incident_date=datetime.date(2026, 5, 14),
            defaults={
                'description': 'Minor speed ticket in Bishkek center. Cleared later.',
                'reported_by': company_user
            }
        )

        # 7. Driver Rating
        DriverRating.objects.get_or_create(
            driver=driver,
            rated_by=superadmin,
            defaults={
                'rating': 4.8,
                'admin_comments': 'Excellent punctuality and good vehicle care.',
                'user_comments': 'Very polite driver, on time always.'
            }
        )

        # 8. Subscription for Company
        premium_plan = Plan.objects.filter(slug='premium-plan').first()
        if premium_plan:
            Subscription.objects.get_or_create(
                user=company_user,
                plan=premium_plan,
                defaults={
                    'start_date': timezone.now() - datetime.timedelta(days=10),
                    'end_date': timezone.now() + datetime.timedelta(days=20),
                    'status': Subscription.Status.ACTIVE
                }
            )

        self.stdout.write(self.style.SUCCESS('Seeded all 3 roles: Super Admin, Fleet Admin, and Driver!'))
