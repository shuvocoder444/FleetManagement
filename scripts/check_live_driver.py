import paramiko

key = paramiko.RSAKey.from_private_key_file(r'C:\Users\shuvo\.ssh\id_rsa')
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('195.250.26.201', username='webkoders', pkey=key, timeout=20)

remote_code = """
from apps.accounts.models import CustomUser
u = CustomUser.objects.filter(email='driver@topd.kg').first()
if u:
    print('Remote user:', u.email, 'role:', u.role, 'is_active:', u.is_active, 'status:', u.status)
    print('Remote check_password:', u.check_password('driver123'))
else:
    print('Remote user driver@topd.kg NOT FOUND!')
"""

stdin, stdout, stderr = ssh.exec_command('/home/webkoders/virtualenv/rus.velohoster.com/3.12/bin/python /home/webkoders/rus.velohoster.com/manage.py shell')
stdin.write(remote_code)
stdin.close()
print("STDOUT:", stdout.read().decode())
print("STDERR:", stderr.read().decode())
ssh.close()

