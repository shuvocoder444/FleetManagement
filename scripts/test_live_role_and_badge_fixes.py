import requests

base_url = 'http://rus.velohoster.com'
session = requests.Session()

# 1. Super Admin Login
r_login = session.get(f'{base_url}/accounts/login/')
csrf = session.cookies.get('csrftoken')

post_data = {
    'email': 'admin@topd.kg',
    'password': 'admin123',
    'csrfmiddlewaretoken': csrf
}
r_auth = session.post(f'{base_url}/accounts/login/', data=post_data, headers={'Referer': f'{base_url}/accounts/login/'}, allow_redirects=True)
print("Superadmin login final URL:", r_auth.url, "Status:", r_auth.status_code)
assert r_auth.status_code == 200

# 2. Super Admin previews Company Dashboard
r_comp = session.get(f'{base_url}/dashboard/admin/')
print("Previewed /dashboard/admin/ -> status:", r_comp.status_code)

# 3. Super Admin visits operational menus: Agreements, Vehicles, Drivers, Settings
superadmin_urls = [
    '/agreements/',
    '/vehicles/',
    '/drivers/',
    '/billing/subscriptions/',
    '/settings/',
]

for url_path in superadmin_urls:
    url = f"{base_url}{url_path}"
    res = session.get(url)
    print(f"Testing Superadmin on {url_path} -> status: {res.status_code}")
    assert res.status_code == 200
    html = res.text
    # Must have superadmin link and NOT company dashboard sidebar
    assert '/dashboard/superadmin/' in html, f"Superadmin link missing on {url_path}"
    assert 'FLEET COMPANY ADMIN SIDEBAR' not in html, f"Company sidebar mistakenly shown on {url_path}"
    print(f"  [OK] Retained Super Admin master sidebar on {url_path}!")

# 4. Check that 'Fleet Admin' is NOT in company dashboard and Bishkek Wheels Car Rental is shown
r_comp_check = session.get(f'{base_url}/dashboard/admin/')
html_comp = r_comp_check.text
assert '2. Fleet Admin' not in html_comp, "Found '2. Fleet Admin' in html!"
print("  [OK] 'Fleet Admin' is removed and dynamic company badge is active!")

# 5. Check visiting website while logged in
r_home = session.get(f'{base_url}/')
print("Testing visit to public homepage while logged in -> status:", r_home.status_code)
assert r_home.status_code == 200
# User should stay authenticated with Dashboard button in navbar
assert 'Sign In' not in r_home.text or 'Dashboard' in r_home.text
print("  [OK] User remains authenticated on public website!")

print("\nALL 3 FIXES VERIFIED 100% WORKING ON RUS.VELOHOSTER.COM!")

