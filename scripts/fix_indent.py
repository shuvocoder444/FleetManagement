with open(r'D:\new\apps\agreements\views.py', 'r', encoding='utf-8') as f:
    c = f.read().replace('\r\n', '\n')

c = c.replace('                        messages.success', '            messages.success')

with open(r'D:\new\apps\agreements\views.py', 'w', encoding='utf-8') as f:
    f.write(c)

print('Indentation fixed in apps/agreements/views.py')
