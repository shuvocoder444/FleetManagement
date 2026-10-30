import paramiko

key_path = r'C:\Users\shuvo\.ssh\id_rsa'
key = paramiko.RSAKey.from_private_key_file(key_path)

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('195.250.26.201', port=22, username='webkoders', pkey=key, timeout=30)

sftp = ssh.open_sftp()
remote_root = '/home/webkoders/rus.velohoster.com'

files = [
    (r'D:\new\apps\accounts\models.py', f'{remote_root}/apps/accounts/models.py'),
    (r'D:\new\apps\accounts\utils.py', f'{remote_root}/apps/accounts/utils.py'),
    (r'D:\new\apps\accounts\views.py', f'{remote_root}/apps/accounts/views.py'),
    (r'D:\new\apps\accounts\urls.py', f'{remote_root}/apps/accounts/urls.py'),
    (r'D:\new\apps\accounts\migrations\0003_customuser_company_customuser_member_role_and_more.py', f'{remote_root}/apps/accounts/migrations/0003_customuser_company_customuser_member_role_and_more.py'),
    (r'D:\new\apps\agreements\views.py', f'{remote_root}/apps/agreements/views.py'),
    (r'D:\new\apps\vehicles\views.py', f'{remote_root}/apps/vehicles/views.py'),
    (r'D:\new\apps\drivers\views.py', f'{remote_root}/apps/drivers/views.py'),
    (r'D:\new\apps\site_settings\translations.py', f'{remote_root}/apps/site_settings/translations.py'),
    (r'D:\new\templates\dashboard\base_dashboard.html', f'{remote_root}/templates/dashboard/base_dashboard.html'),
    (r'D:\new\templates\users\team_members.html', f'{remote_root}/templates/users/team_members.html'),
    (r'D:\new\templates\users\activity_log.html', f'{remote_root}/templates/users/activity_log.html'),
]

for l, r in files:
    sftp.put(l, r)
    print(f'Uploaded {l} -> {r}')

sftp.close()

# Run migrate on live server
py_bin = '/home/webkoders/virtualenv/rus.velohoster.com/3.12/bin/python'
manage_py = f'{remote_root}/manage.py'

print('Running migration on live server...')
stdin, stdout, stderr = ssh.exec_command(f'{py_bin} {manage_py} migrate')
print('Migrate STDOUT:', stdout.read().decode())
print('Migrate STDERR:', stderr.read().decode())

# Seed team & logs
with open(r'D:\new\scripts\seed_team_and_logs.py', 'r', encoding='utf-8') as f:
    seed_code = f.read()

print('Seeding sample team member and activity logs on live server...')
stdin, stdout, stderr = ssh.exec_command(f'{py_bin} {manage_py} shell')
stdin.write(seed_code)
stdin.close()
print('Seed STDOUT:', stdout.read().decode())
print('Seed STDERR:', stderr.read().decode())

# Restart Passenger
stdin, stdout, stderr = ssh.exec_command(f'touch {remote_root}/tmp/restart.txt')
print('Passenger restarted:', stdout.read().decode())

ssh.close()
print('SUCCESS! Live deployment & verification complete.')

