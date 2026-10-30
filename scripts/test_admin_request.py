import paramiko

key = paramiko.RSAKey.from_private_key_file(r'C:\Users\shuvo\.ssh\id_rsa')
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('195.250.26.201', username='webkoders', pkey=key)

cmd = (
    "/home/webkoders/virtualenv/rus.velohoster.com/3.12/bin/python "
    "/home/webkoders/rus.velohoster.com/manage.py shell -c \""
    "from django.test import RequestFactory; "
    "from apps.dashboard.views import admin_dashboard, dashboard_router; "
    "from apps.accounts.models import CustomUser; "
    "from django.contrib.sessions.middleware import SessionMiddleware; "
    "u = CustomUser.objects.get(email='bakyt@bishkekwheels.kg'); "
    "rf = RequestFactory(); "
    "req = rf.get('/dashboard/admin/'); "
    "req.user = u; "
    "middleware = SessionMiddleware(lambda r: None); "
    "middleware.process_request(req); "
    "req.session.save(); "
    "res = admin_dashboard(req); "
    "print('STATUS:', res.status_code); "
    "print('SESSION ROLE:', req.session.get('active_dashboard_role')); "
    "\""
)
stdin, stdout, stderr = ssh.exec_command(cmd)
print("STDOUT:", stdout.read().decode('utf-8'))
print("STDERR:", stderr.read().decode('utf-8'))
ssh.close()

