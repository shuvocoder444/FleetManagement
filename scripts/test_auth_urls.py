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

u = CustomUser.objects.filter(is_superuser=True).first()
c = Client()
c.force_login(u)

urls = [
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

for url in urls:
    r = c.get(url)
    user = r.wsgi_request.user
    print(f"{url:25} -> status: {r.status_code}, auth: {user.is_authenticated}, email: {getattr(user, 'email', None)}")
    assert user.is_authenticated, f"Unauthenticated at {url}"
