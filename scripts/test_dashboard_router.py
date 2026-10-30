import os, sys
sys.path.insert(0, r'D:\new')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import django
django.setup()

from django.test import RequestFactory
from django.contrib.sessions.middleware import SessionMiddleware
from apps.accounts.models import CustomUser
from apps.site_settings.context_processors import site_settings_processor, get_active_dashboard_role
from apps.dashboard.views import dashboard_router

users = [
    CustomUser.objects.get(email='bakyt@bishkekwheels.kg'),
    CustomUser.objects.get(email='admin@topd.kg'),
    None,
]

rf = RequestFactory()

for u in users:
    email = u.email if u else 'Anonymous'
    print(f"\n=== Testing fresh visit to /dashboard/ for {email} ===")
    req = rf.get('/dashboard/')
    if u:
        req.user = u
    else:
        from django.contrib.auth.models import AnonymousUser
        req.user = AnonymousUser()
    middleware = SessionMiddleware(lambda r: None)
    middleware.process_request(req)
    req.session.save()
    res = dashboard_router(req)
    print(f"Redirect location: {res.url}")

