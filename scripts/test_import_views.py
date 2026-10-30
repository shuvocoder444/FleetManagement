import paramiko

key = paramiko.RSAKey.from_private_key_file(r'C:\Users\shuvo\.ssh\id_rsa')
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('195.250.26.201', username='webkoders', pkey=key, timeout=20)

cmd = """/home/webkoders/virtualenv/rus.velohoster.com/3.12/bin/python -c "
import sys
sys.path.insert(0, '/home/webkoders/rus.velohoster.com')
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import django
django.setup()
import apps.dashboard.views as v
print('dashboard_router in v?', hasattr(v, 'dashboard_router'))
print('v dir:', [x for x in dir(v) if not x.startswith('_')])
" """

stdin, stdout, stderr = ssh.exec_command(cmd)
print("STDOUT:", stdout.read().decode())
print("STDERR:", stderr.read().decode())
ssh.close()

