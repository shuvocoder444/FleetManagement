import os, sys
sys.path.insert(0, r'D:\new')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import django
django.setup()

from django.test import RequestFactory
from django.contrib.sessions.middleware import SessionMiddleware
from apps.accounts.models import CustomUser
from apps.site_settings.context_processors import site_settings_processor, get_active_dashboard_role
from apps.vehicles.views import vehicle_list
from apps.agreements.views import agreement_list
from apps.drivers.views import driver_list, check_driver_view
from apps.billing.views import subscriptions_list, purchase_subscription
from apps.dashboard.views import admin_dashboard, superadmin_dashboard

users = [
    CustomUser.objects.get(email='bakyt@bishkekwheels.kg'),
    CustomUser.objects.get(email='admin@topd.kg'),
]

urls_and_views = [
    ('/dashboard/admin/', admin_dashboard),
    ('/vehicles/', vehicle_list),
    ('/agreements/', agreement_list),
    ('/drivers/', driver_list),
    ('/drivers/check/', check_driver_view),
    ('/billing/subscriptions/', subscriptions_list),
    ('/billing/purchase/', purchase_subscription),
]

rf = RequestFactory()

for u in users:
    print(f"\n=== Testing for user: {u.email} (role={u.role}, is_superuser={u.is_superuser}) ===")
    for path, view_func in urls_and_views:
        req = rf.get(path)
        req.user = u
        middleware = SessionMiddleware(lambda r: None)
        middleware.process_request(req)
        # simulate session active role if already in admin
        req.session['active_dashboard_role'] = 'admin'
        req.session.save()
        res = view_func(req)
        ctx_role = req.session.get('active_dashboard_role')
        proc_role = get_active_dashboard_role(req)
        print(f"Path: {path:25} -> Status: {res.status_code}, Session Role: {ctx_role}, Context Role: {proc_role}")
