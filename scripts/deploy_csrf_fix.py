import paramiko

key_path = r'C:\Users\shuvo\.ssh\id_rsa'
key = paramiko.RSAKey.from_private_key_file(key_path)

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('195.250.26.201', port=22, username='webkoders', pkey=key, timeout=20)

sftp = ssh.open_sftp()
remote_root = '/home/webkoders/rus.velohoster.com'

files = [
    (r'D:\new\config\settings.py', f'{remote_root}/config/settings.py'),
    (r'D:\new\apps\accounts\views.py', f'{remote_root}/apps/accounts/views.py'),
    (r'D:\new\apps\site_settings\middleware.py', f'{remote_root}/apps/site_settings/middleware.py'),
    (r'D:\new\templates\users\login.html', f'{remote_root}/templates/users/login.html'),
]

for l, r in files:
    sftp.put(l, r)
    print(f'Uploaded {l} -> {r}')

sftp.close()

stdin, stdout, stderr = ssh.exec_command(f'touch {remote_root}/tmp/restart.txt')
print('Passenger restarted:', stdout.read().decode())
ssh.close()
print('SUCCESS!')

