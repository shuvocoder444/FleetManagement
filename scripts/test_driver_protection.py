import os, sys
sys.path.insert(0, r'D:\new')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import django
django.setup()

from django.test import Client

c = Client()

# 1. Login with next=/dashboard/admin/
res = c.post('/accounts/login/?next=/dashboard/admin/', {'email': 'driver@topd.kg', 'password': 'driver123'}, follow=False)
print("1. Login POST redirect location:", res.get('Location'))
assert res.get('Location') == '/dashboard/driver/', f"Expected /dashboard/driver/, got {res.get('Location')}"

# 2. Visit /dashboard/ while logged in as driver
res2 = c.get('/dashboard/', follow=False)
print("2. /dashboard/ redirect location:", res2.get('Location'))
assert res2.get('Location') == '/dashboard/driver/', f"Expected /dashboard/driver/, got {res2.get('Location')}"

# 3. Try to access /dashboard/admin/ while logged in as driver
res3 = c.get('/dashboard/admin/', follow=False)
print("3. /dashboard/admin/ redirect location:", res3.get('Location'))
assert res3.get('Location') == '/dashboard/driver/', f"Expected /dashboard/driver/, got {res3.get('Location')}"

# 4. Try to access /dashboard/superadmin/ while logged in as driver
res4 = c.get('/dashboard/superadmin/', follow=False)
print("4. /dashboard/superadmin/ redirect location:", res4.get('Location'))
assert res4.get('Location') == '/dashboard/driver/', f"Expected /dashboard/driver/, got {res4.get('Location')}"

# 5. Load /dashboard/driver/
res5 = c.get('/dashboard/driver/')
print("5. /dashboard/driver/ status:", res5.status_code)
assert res5.status_code == 200

print("\nALL DRIVER ROUTING & PROTECTION TESTS PASSED SUCCESSFULLY!")

