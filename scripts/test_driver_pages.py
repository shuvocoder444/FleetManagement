import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.test import Client
from apps.accounts.models import CustomUser

client = Client()

# Test anonymous / direct access
urls = [
    '/dashboard/driver/',
    '/dashboard/driver/vehicle/',
    '/dashboard/driver/agreements/',
    '/dashboard/driver/history/',
]

print("--- Testing Anonymous Access ---")
for url in urls:
    resp = client.get(url)
    print(f"{url} -> status {resp.status_code}")
    assert resp.status_code == 200, f"Expected 200 for {url}, got {resp.status_code}"

print("\n--- Testing Logged In Driver (driver@topd.kg) ---")
login_success = client.login(username='driver@topd.kg', password='driver123')
print("Login success:", login_success)
assert login_success, "Failed to login as driver@topd.kg"

for url in urls:
    resp = client.get(url)
    print(f"{url} -> status {resp.status_code}")
    assert resp.status_code == 200, f"Expected 200 for {url}, got {resp.status_code}"

# Test query parameters on agreements page
resp = client.get('/dashboard/driver/agreements/?status=active')
print(f"/dashboard/driver/agreements/?status=active -> status {resp.status_code}")
assert resp.status_code == 200

resp = client.get('/dashboard/driver/agreements/?status=completed')
print(f"/dashboard/driver/agreements/?status=completed -> status {resp.status_code}")
assert resp.status_code == 200

print("\nALL DRIVER PAGES PASSED SUCCESSFULLY!")
