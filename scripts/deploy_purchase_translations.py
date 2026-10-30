import paramiko

key_path = r'C:\Users\shuvo\.ssh\id_rsa'
key = paramiko.RSAKey.from_private_key_file(key_path)

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('195.250.26.201', port=22, username='webkoders', pkey=key, timeout=20)

sftp = ssh.open_sftp()
remote_root = '/home/webkoders/rus.velohoster.com'

files = [
    (r'D:\new\apps\site_settings\translations.py', f'{remote_root}/apps/site_settings/translations.py'),
    (r'D:\new\templates\billing\purchase.html', f'{remote_root}/templates/billing/purchase.html'),
    (r'D:\new\templates\billing\subscriptions.html', f'{remote_root}/templates/billing/subscriptions.html'),
    (r'D:\new\templates\dashboard\base_dashboard.html', f'{remote_root}/templates/dashboard/base_dashboard.html'),
]

for l, r in files:
    sftp.put(l, r)
    print(f'Uploaded {l} -> {r}')

sftp.close()

# Clean pycache & kill stale lswsgi workers
commands = [
    f'find {remote_root}/apps -type d -name "__pycache__" -exec rm -rf {{}} +',
    'pkill -9 -f "rus.velohoster.com/passenger_wsgi.py"',
    f'touch {remote_root}/tmp/restart.txt',
]

for cmd in commands:
    stdin, stdout, stderr = ssh.exec_command(cmd)
    stdout.read()

ssh.close()
print('SUCCESS! Deployed purchase translations & restarted lswsgi.')
