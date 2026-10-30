import paramiko

key = paramiko.RSAKey.from_private_key_file(r'C:\Users\shuvo\.ssh\id_rsa')
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('195.250.26.201', username='webkoders', pkey=key)
stdin, stdout, stderr = ssh.exec_command("sed -n '295,330p' /home/webkoders/rus.velohoster.com/templates/dashboard/base_dashboard.html")
print(stdout.read().decode('utf-8'))
ssh.close()

