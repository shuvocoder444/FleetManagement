import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import django
django.setup()

from django.test import Client
from apps.accounts.models import CustomUser

client = Client()
client.login(username='superadmin@topd.kg', password='adminpassword')

urls_to_test = [
    '/',
    '/about/',
    '/features/',
    '/pricing/',
    '/contact/',
    '/terms/',
    '/privacy/',
    '/dashboard/superadmin/',
    '/dashboard/',
]

print("--- Testing Superadmin Session Across Website Pages ---")
for u in urls_to_test:
    r = client.get(u)
    user = r.wsgi_request.user
    print(f"URL: {u:25} -> status: {r.status_code}, authenticated: {user.is_authenticated}, email: {getattr(user, 'email', None)}")
    assert user.is_authenticated, f"User became unauthenticated on {u}!"
