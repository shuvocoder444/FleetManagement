import os, sys
sys.path.insert(0, r'D:\new')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import django
django.setup()

from django.test import RequestFactory
from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.messages.middleware import MessageMiddleware
from django.contrib.messages import get_messages
from apps.accounts.models import CustomUser
from apps.accounts.views import logout_view, clear_messages
import django.contrib.messages as dj_messages

company = CustomUser.objects.get(email='bakyt@bishkekwheels.kg')
rf = RequestFactory()

req = rf.get('/accounts/logout/')
req.user = company
SessionMiddleware(lambda r: None).process_request(req)
MessageMiddleware(lambda r: None).process_request(req)

# Simulate 3 previous accumulated messages
dj_messages.success(req, "Welcome back, Team!")
dj_messages.success(req, "Team member Shuvo Ahammed added successfully (2/3 seats used)!")
dj_messages.info(req, "Old notice")

# Call logout_view
res = logout_view(req)
print("Logout redirect to:", res.url)

# Check messages remaining for next request (landing page)
remaining = [m.message for m in get_messages(req)]
print("Messages for landing page:", remaining)

assert len(remaining) == 1, f"Expected 1 message, got {len(remaining)}: {remaining}"
assert remaining[0] == 'You have been logged out successfully.'
print("SUCCESS: Only the single logout notification is displayed!")
