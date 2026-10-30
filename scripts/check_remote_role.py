import paramiko

key = paramiko.RSAKey.from_private_key_file(r'C:\Users\shuvo\.ssh\id_rsa')
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('195.250.26.201', username='webkoders', pkey=key)

cmd = (
    "/home/webkoders/virtualenv/rus.velohoster.com/3.12/bin/python "
    "/home/webkoders/rus.velohoster.com/manage.py shell -c \""
    "from apps.site_settings.context_processors import get_active_dashboard_role; "
    "from apps.accounts.models import CustomUser; "
    "from django.test import RequestFactory; "
    "from django.contrib.sessions.middleware import SessionMiddleware; "
    "u = CustomUser.objects.get(email='bakyt@bishkekwheels.kg'); "
    "rf = RequestFactory(); "
    "req = rf.get('/agreements/'); "
    "req.user = u; "
    "SessionMiddleware(lambda r: None).process_request(req); "
    "role = get_active_dashboard_role(req); "
    "print('Agreements role for Bakyt:', role); "
    "\""
)
stdin, stdout, stderr = ssh.exec_command(cmd)
print("STDOUT:", stdout.read().decode('utf-8'))
print("STDERR:", stderr.read().decode('utf-8'))
ssh.close()

