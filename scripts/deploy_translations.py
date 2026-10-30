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
    (r'D:\new\templates\landing\base_frontend.html', f'{remote_root}/templates/landing/base_frontend.html'),
    (r'D:\new\templates\landing\index.html', f'{remote_root}/templates/landing/index.html'),
    (r'D:\new\templates\landing\about.html', f'{remote_root}/templates/landing/about.html'),
    (r'D:\new\templates\landing\features.html', f'{remote_root}/templates/landing/features.html'),
    (r'D:\new\templates\landing\pricing.html', f'{remote_root}/templates/landing/pricing.html'),
    (r'D:\new\templates\landing\contact.html', f'{remote_root}/templates/landing/contact.html'),
    (r'D:\new\templates\landing\terms.html', f'{remote_root}/templates/landing/terms.html'),
    (r'D:\new\templates\landing\privacy.html', f'{remote_root}/templates/landing/privacy.html'),
]

for l, r in files:
    sftp.put(l, r)
    print(f'Uploaded {l} -> {r}')

sftp.close()

stdin, stdout, stderr = ssh.exec_command(f'touch {remote_root}/tmp/restart.txt')
print('Passenger restarted:', stdout.read().decode())
ssh.close()
print('SUCCESS! All translations deployed to live server.')
