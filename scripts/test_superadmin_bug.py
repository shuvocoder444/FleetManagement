import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import django
django.setup()

from django.test import Client

c = Client()
c.login(username='admin@topd.kg', password='admin123')

# 1. Super admin visits /dashboard/admin/
c.get('/dashboard/admin/')

# 2. Super admin visits /agreements/
r = c.get('/agreements/')
html = r.content.decode('utf-8')
if 'Company Dashboard' in html:
    print("BUG CONFIRMED: Superadmin sees 'Company Dashboard' sidebar after clicking agreements!")
elif 'Super Admin Dashboard' in html:
    print("OK: Superadmin sees Super Admin Dashboard sidebar")
else:
    print("Neither found in html")

