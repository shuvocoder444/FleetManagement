import paramiko

key = paramiko.RSAKey.from_private_key_file(r'C:\Users\shuvo\.ssh\id_rsa')
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('195.250.26.201', username='webkoders', pkey=key, timeout=20)

remote_test = """
from django.test import Client

c = Client()
c.login(username='driver@topd.kg', password='driver123')
res = c.get('/dashboard/driver/')
print('Status code:', res.status_code)
if res.status_code in [301, 302]:
    print('Redirects to:', res.get('Location'))
"""

stdin, stdout, stderr = ssh.exec_command('/home/webkoders/virtualenv/rus.velohoster.com/3.12/bin/python /home/webkoders/rus.velohoster.com/manage.py shell')
stdin.write(remote_test)
stdin.close()
print("STDOUT:", stdout.read().decode())
print("STDERR:", stderr.read().decode())
ssh.close()

