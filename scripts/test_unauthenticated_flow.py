import paramiko

key = paramiko.RSAKey.from_private_key_file(r'C:\Users\shuvo\.ssh\id_rsa')
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('195.250.26.201', username='webkoders', pkey=key)

remote_test = """
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

# Step 1: User visits /dashboard/admin/
req1 = rf.get('/dashboard/admin/')
req1.user = AnonymousUser()
sm = SessionMiddleware(lambda r: None)
sm.process_request(req1)
admin_dashboard(req1)
req1.session.save()

session_key = req1.session.session_key
role_after_admin = req1.session.get('active_dashboard_role')
print('Role after /dashboard/admin/:', role_after_admin)

# Step 2: Now user navigates with this session cookie to other pages
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
    print(f'{url:25} -> status: {res.status_code}, redirect: {redirect_to}, ctx_role: {role_in_ctx}, processor_role: {sp_ctx.get(\"current_dashboard\")}')
"""

cmd = (
    "/home/webkoders/virtualenv/rus.velohoster.com/3.12/bin/python "
    "/home/webkoders/rus.velohoster.com/manage.py shell"
)
stdin, stdout, stderr = ssh.exec_command(cmd)
stdin.write(remote_test)
stdin.close()
print("STDOUT:", stdout.read().decode('utf-8'))
print("STDERR:", stderr.read().decode('utf-8'))
ssh.close()
