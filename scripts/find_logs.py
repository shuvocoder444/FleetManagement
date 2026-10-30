import paramiko

key = paramiko.RSAKey.from_private_key_file(r'C:\Users\shuvo\.ssh\id_rsa')
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('195.250.26.201', username='webkoders', pkey=key, timeout=20)

stdin, stdout, stderr = ssh.exec_command('ls -la /home/webkoders/rus.velohoster.com ; ls -la /home/webkoders/logs ; ls -la /home/webkoders')
print(stdout.read().decode())
print(stderr.read().decode())
ssh.close()

