import paramiko

key = paramiko.RSAKey.from_private_key_file(r'C:\Users\shuvo\.ssh\id_rsa')
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('195.250.26.201', username='webkoders', pkey=key, timeout=20)

stdin, stdout, stderr = ssh.exec_command('tail -n 30 /home/webkoders/rus.velohoster.com/stderr.log')
print("Tail 30 lines:")
print(stdout.read().decode())
ssh.close()

