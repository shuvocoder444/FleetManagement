import paramiko

key = paramiko.RSAKey.from_private_key_file(r'C:\Users\shuvo\.ssh\id_rsa')
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('195.250.26.201', username='webkoders', pkey=key, timeout=20)

remote_test = """
from django.test import Client

c = Client()
login_res = c.post('/accounts/login/', {'email': 'driver@topd.kg', 'password': 'driver123'})
print("Login redirect:", login_res.get('Location'))

urls = [
    '/dashboard/driver/',
    '/dashboard/driver/vehicle/',
    '/dashboard/driver/agreements/',
    '/dashboard/driver/history/',
]

for u in urls:
    res = c.get(u)
    print(u, 'status:', res.status_code)
    assert res.status_code == 200, f'Failed {u}'
    html = res.content.decode('utf-8')
    assert '/dashboard/driver/vehicle/' in html, f'vehicle link not in {u}'
    assert '/dashboard/driver/agreements/' in html, f'agreements link not in {u}'
    assert '/dashboard/driver/history/' in html, f'history link not in {u}'

print('ALL 4 DRIVER MENU PAGES VERIFIED 100% OK ON LIVE DJANGO!')
"""

stdin, stdout, stderr = ssh.exec_command('/home/webkoders/virtualenv/rus.velohoster.com/3.12/bin/python /home/webkoders/rus.velohoster.com/manage.py shell')
stdin.write(remote_test)
stdin.close()
print("STDOUT:", stdout.read().decode())
print("STDERR:", stderr.read().decode())
ssh.close()

