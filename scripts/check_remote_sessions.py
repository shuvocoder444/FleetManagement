import paramiko

key = paramiko.RSAKey.from_private_key_file(r'C:\Users\shuvo\.ssh\id_rsa')
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('195.250.26.201', username='webkoders', pkey=key)

remote_script = """
from django.contrib.sessions.models import Session
from django.utils import timezone
from apps.accounts.models import CustomUser

sessions = Session.objects.filter(expire_date__gte=timezone.now()).order_by('-expire_date')
print('Total active sessions:', sessions.count())
for s in sessions[:15]:
    try:
        data = s.get_decoded()
        uid = data.get('_auth_user_id')
        role = data.get('active_dashboard_role')
        user = CustomUser.objects.filter(id=uid).first() if uid else None
        print(s.session_key[:8], 'UID:', uid, 'User:', user.email if user else None, 'Role:', role)
    except Exception as e:
        print('Error decoding session:', e)
"""

cmd = (
    "/home/webkoders/virtualenv/rus.velohoster.com/3.12/bin/python "
    "/home/webkoders/rus.velohoster.com/manage.py shell"
)
stdin, stdout, stderr = ssh.exec_command(cmd)
stdin.write(remote_script)
stdin.close()
print("STDOUT:", stdout.read().decode('utf-8'))
print("STDERR:", stderr.read().decode('utf-8'))
ssh.close()
