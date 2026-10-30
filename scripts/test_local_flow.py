import os, sys
sys.path.insert(0, r'D:\new')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import django
django.setup()

from django.test import RequestFactory
from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.auth.models import AnonymousUser
from apps.site_settings.context_processors import get_active_dashboard_role, site_settings_processor
from apps.dashboard.views import admin_dashboard, dashboard_router
from apps.vehicles.views import vehicle_list
from apps.agreements.views import agreement_list
from apps.drivers.views import driver_list, check_driver_view
from apps.billing.views import subscriptions_list, purchase_subscription

rf = RequestFactory()

req1 = rf.get('/dashboard/admin/')
req1.user = AnonymousUser()
sm = SessionMiddleware(lambda r: None)
sm.process_request(req1)
admin_dashboard(req1)
req1.session.save()

session_key = req1.session.session_key
role_after_admin = req1.session.get('active_dashboard_role')
print('Role after /dashboard/admin/:', role_after_admin)

urls = [
    ('/dashboard/admin/', admin_dashboard),
    ('/vehicles/', vehicle_list),
    ('/agreements/', agreement_list),
    ('/drivers/', driver_list),
    ('/drivers/check/', check_driver_view),
    ('/billing/subscriptions/', subscriptions_list),
    ('/billing/purchase/', purchase_subscription),
    ('/dashboard/', dashboard_router),
]

for url, view_fn in urls:
    req = rf.get(url)
    req.user = AnonymousUser()
    req.COOKIES['sessionid'] = session_key
    sm.process_request(req)
    res = view_fn(req)
    role_in_ctx = get_active_dashboard_role(req)
    sp_ctx = site_settings_processor(req)
    redirect_to = getattr(res, 'url', None)
    print(f"{url:25} -> status: {res.status_code}, redirect: {redirect_to}, ctx_role: {role_in_ctx}, processor_role: {sp_ctx.get('current_dashboard')}")

