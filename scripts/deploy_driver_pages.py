import paramiko

key_path = r'C:\Users\shuvo\.ssh\id_rsa'
key = paramiko.RSAKey.from_private_key_file(key_path)

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('195.250.26.201', port=22, username='webkoders', pkey=key, timeout=20)

sftp = ssh.open_sftp()
remote_root = '/home/webkoders/rus.velohoster.com'

files = [
    (r'D:\new\apps\dashboard\urls.py', f'{remote_root}/apps/dashboard/urls.py'),
    (r'D:\new\apps\dashboard\views.py', f'{remote_root}/apps/dashboard/views.py'),
    (r'D:\new\templates\dashboard\base_dashboard.html', f'{remote_root}/templates/dashboard/base_dashboard.html'),
    (r'D:\new\templates\dashboard\driver.html', f'{remote_root}/templates/dashboard/driver.html'),
    (r'D:\new\templates\dashboard\driver_vehicle.html', f'{remote_root}/templates/dashboard/driver_vehicle.html'),
    (r'D:\new\templates\dashboard\driver_agreements.html', f'{remote_root}/templates/dashboard/driver_agreements.html'),
    (r'D:\new\templates\dashboard\driver_history.html', f'{remote_root}/templates/dashboard/driver_history.html'),
]

for l, r in files:
    sftp.put(l, r)
    print(f'Uploaded {l} -> {r}')

sftp.close()

stdin, stdout, stderr = ssh.exec_command(f'touch {remote_root}/tmp/restart.txt')
print('Passenger restarted:', stdout.read().decode())
ssh.close()
print('SUCCESS! All driver dedicated pages deployed to rus.velohoster.com.')
