import paramiko

key = paramiko.RSAKey.from_private_key_file(r'C:\Users\shuvo\.ssh\id_rsa')
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('195.250.26.201', username='webkoders', pkey=key, timeout=20)

remote_test = """
from django.test import Client

c = Client()

# 1. Login with next=/dashboard/admin/
res = c.post('/accounts/login/?next=/dashboard/admin/', {'email': 'driver@topd.kg', 'password': 'driver123'}, follow=False)
print("1. Live login POST redirect location:", res.get('Location'))
assert res.get('Location') == '/dashboard/driver/'

# 2. Visit /dashboard/ while logged in as driver
res2 = c.get('/dashboard/', follow=False)
print("2. Live /dashboard/ redirect location:", res2.get('Location'))
assert res2.get('Location') == '/dashboard/driver/'

# 3. Try to access /dashboard/admin/ while logged in as driver
res3 = c.get('/dashboard/admin/', follow=False)
print("3. Live /dashboard/admin/ redirect location:", res3.get('Location'))
assert res3.get('Location') == '/dashboard/driver/'

# 4. Try to access /dashboard/superadmin/ while logged in as driver
res4 = c.get('/dashboard/superadmin/', follow=False)
print("4. Live /dashboard/superadmin/ redirect location:", res4.get('Location'))
assert res4.get('Location') == '/dashboard/driver/'

# 5. Load /dashboard/driver/
res5 = c.get('/dashboard/driver/')
print("5. Live /dashboard/driver/ status:", res5.status_code)
assert res5.status_code == 200

print("ALL LIVE TESTS PASSED 100%!")
"""

stdin, stdout, stderr = ssh.exec_command('/home/webkoders/virtualenv/rus.velohoster.com/3.12/bin/python /home/webkoders/rus.velohoster.com/manage.py shell')
stdin.write(remote_test)
stdin.close()
print("STDOUT:", stdout.read().decode())
print("STDERR:", stderr.read().decode())
ssh.close()
