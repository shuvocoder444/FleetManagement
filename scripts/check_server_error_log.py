import paramiko

key = paramiko.RSAKey.from_private_key_file(r'C:\Users\shuvo\.ssh\id_rsa')
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('195.250.26.201', username='webkoders', pkey=key, timeout=20)

commands = [
    'tail -n 50 /home/webkoders/rus.velohoster.com/logs/error.log',
    'tail -n 50 /home/webkoders/rus.velohoster.com/passenger.log',
    'tail -n 50 /var/log/apache2/error.log',
    'tail -n 50 /home/webkoders/rus.velohoster.com/tmp/passenger.*.log'
]

for cmd in commands:
    print(f"=== {cmd} ===")
    stdin, stdout, stderr = ssh.exec_command(cmd)
    out = stdout.read().decode()
    err = stderr.read().decode()
    if out:
        print("OUT:", out)
    if err:
        print("ERR:", err)

ssh.close()

