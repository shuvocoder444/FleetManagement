import paramiko

key = paramiko.RSAKey.from_private_key_file(r'C:\Users\shuvo\.ssh\id_rsa')
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('195.250.26.201', username='webkoders', pkey=key, timeout=20)

remote_code = """
from apps.accounts.models import CustomUser
from apps.drivers.models import Driver

print("=== ALL USERS ===")
for u in CustomUser.objects.all():
    print(f"ID: {u.id}, Email: '{u.email}', Role: {u.role}, Active: {u.is_active}, Status: {u.status}")

# Explicitly ensure driver123 is set
d_user = CustomUser.objects.filter(email='driver@topd.kg').first()
if d_user:
    d_user.set_password('driver123')
    d_user.is_active = True
    d_user.status = CustomUser.Status.VERIFIED
    d_user.save()
    print("Explicitly reset driver@topd.kg password to 'driver123' and saved!")

print("=== ALL DRIVERS IN DRIVER MODEL ===")
for d in Driver.objects.all():
    print(f"Driver ID: {d.id}, Name: {d.full_name}, Phone: {d.phone}, Email: {d.email}")
"""

stdin, stdout, stderr = ssh.exec_command('/home/webkoders/virtualenv/rus.velohoster.com/3.12/bin/python /home/webkoders/rus.velohoster.com/manage.py shell')
stdin.write(remote_code)
stdin.close()
print("STDOUT:", stdout.read().decode())
print("STDERR:", stderr.read().decode())

# Also touch restart.txt to ensure workers reload
stdin, stdout, stderr = ssh.exec_command('touch /home/webkoders/rus.velohoster.com/tmp/restart.txt')
print("Restarted:", stdout.read().decode())

ssh.close()

