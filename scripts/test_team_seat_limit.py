import os, sys
sys.path.insert(0, r'D:\new')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import django
django.setup()

from apps.accounts.models import CustomUser, ActivityLog
from django.test import RequestFactory
from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.messages.middleware import MessageMiddleware
from apps.accounts.views import team_members_view

company = CustomUser.objects.get(email='bakyt@bishkekwheels.kg')
print(f"Initial: {company.email} - Seats: {company.team_seat_count}/{company.max_allowed_seats}")

rf = RequestFactory()

# Try adding 2nd member (Seat 3)
req = rf.post('/accounts/team/', {
    'first_name': 'Gulnaz',
    'last_name': 'Dispatcher',
    'email': 'gulnaz.dispatch@bishkekwheels.kg',
    'password': 'Password123!',
    'member_role': 'Dispatcher',
    'phone': '+996 555 777111'
})
req.user = company
SessionMiddleware(lambda r: None).process_request(req)
MessageMiddleware(lambda r: None).process_request(req)
team_members_view(req)

print(f"After adding Gulnaz: Seats: {company.team_seat_count}/{company.max_allowed_seats}")

# Try adding 4th member (Should be BLOCKED because max seats = 3)
req2 = rf.post('/accounts/team/', {
    'first_name': 'Unauthorized',
    'last_name': 'Person',
    'email': 'unauth@bishkekwheels.kg',
    'password': 'Password123!',
    'member_role': 'Staff',
})
req2.user = company
SessionMiddleware(lambda r: None).process_request(req2)
MessageMiddleware(lambda r: None).process_request(req2)
team_members_view(req2)

print(f"After attempting 4th user: Seats: {company.team_seat_count}/{company.max_allowed_seats}")
assert not CustomUser.objects.filter(email='unauth@bishkekwheels.kg').exists(), "4th member should NOT be created!"
print("SUCCESS: 3-Seat hard limit enforced correctly!")

latest_logs = ActivityLog.objects.filter(company=company).order_by('-created_at')[:3]
for l in latest_logs:
    print(f"LOG: [{l.action_type}] {l.actor_name} ({l.actor_role}): {l.description}")

