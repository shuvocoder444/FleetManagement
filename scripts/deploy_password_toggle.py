import paramiko

key_path = r'C:\Users\shuvo\.ssh\id_rsa'
key = paramiko.RSAKey.from_private_key_file(key_path)

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('195.250.26.201', port=22, username='webkoders', pkey=key, timeout=20)

sftp = ssh.open_sftp()
remote_root = '/home/webkoders/rus.velohoster.com'

files = [
    (r'D:\new\templates\users\login.html', f'{remote_root}/templates/users/login.html'),
    (r'D:\new\templates\users\register.html', f'{remote_root}/templates/users/register.html'),
]

for l, r in files:
    sftp.put(l, r)
    print(f'Uploaded {l} -> {r}')

sftp.close()

stdin, stdout, stderr = ssh.exec_command(f'touch {remote_root}/tmp/restart.txt')
print('Passenger restarted:', stdout.read().decode())
ssh.close()
print('SUCCESS! Password show/hide toggle deployed.')
