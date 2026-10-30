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

# 1. Test Company User
company_user = CustomUser.objects.filter(role=CustomUser.Role.COMPANY).first()
company_name = company_user.get_company_account().company_name
print("Company user:", company_user.email, "company_name:", company_name)

c = Client()
c.force_login(company_user)

r = c.get('/dashboard/admin/')
html = r.content.decode('utf-8')
assert 'Fleet Admin' not in html, "Found 'Fleet Admin' in company dashboard!"
assert company_name in html, f"Company name '{company_name}' not found in dashboard!"
assert 'FLEET COMPANY ADMIN SIDEBAR' in html
print("Company user test passed!")

# 2. Test Individual / Personal User
indiv_user = CustomUser.objects.filter(role=CustomUser.Role.INDIVIDUAL).first()
if indiv_user:
    c_indiv = Client()
    c_indiv.force_login(indiv_user)
    r_indiv = c_indiv.get('/dashboard/admin/')
    html_indiv = r_indiv.content.decode('utf-8')
    assert 'Personal' in html_indiv, "Personal not found for individual user!"
    print("Individual user test passed: shows 'Personal'!")

# 3. Test Superadmin
superadmin = CustomUser.objects.filter(is_superuser=True).first()
c_super = Client()
c_super.force_login(superadmin)

# Superadmin visits agreements, vehicles, billing, settings
for path in ['/agreements/', '/vehicles/', '/drivers/', '/billing/subscriptions/', '/settings/']:
    res = c_super.get(path)
    h = res.content.decode('utf-8')
    assert 'SUPER ADMIN SIDEBAR' in h, f"Expected SUPER ADMIN SIDEBAR on {path}"
    assert 'FLEET COMPANY ADMIN SIDEBAR' not in h, f"Did not expect company sidebar on {path}"
    print(f"Superadmin on {path} -> Correctly has SUPER ADMIN SIDEBAR!")

print("\nALL ROLE & SIDEBAR TESTS PASSED 100%!")
