import paramiko

key = paramiko.RSAKey.from_private_key_file(r'C:\Users\shuvo\.ssh\id_rsa')
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('195.250.26.201', username='webkoders', pkey=key, timeout=20)

commands = [
    # Clean pycache
    'find /home/webkoders/rus.velohoster.com/apps -type d -name "__pycache__" -exec rm -rf {} +',
    # Kill existing lswsgi workers for rus.velohoster.com
    'pkill -9 -f "rus.velohoster.com/passenger_wsgi.py"',
    # Touch restart.txt
    'touch /home/webkoders/rus.velohoster.com/tmp/restart.txt',
]

for cmd in commands:
    print(f"Running: {cmd}")
    stdin, stdout, stderr = ssh.exec_command(cmd)
    print("STDOUT:", stdout.read().decode())
    print("STDERR:", stderr.read().decode())

ssh.close()
print("Cleaned pycache and restarted lswsgi processes!")

