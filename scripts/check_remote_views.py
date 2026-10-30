import paramiko

key = paramiko.RSAKey.from_private_key_file(r'C:\Users\shuvo\.ssh\id_rsa')
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('195.250.26.201', username='webkoders', pkey=key, timeout=20)

stdin, stdout, stderr = ssh.exec_command('head -n 25 /home/webkoders/rus.velohoster.com/apps/dashboard/views.py')
print(stdout.read().decode())
ssh.close()

