import requests

session = requests.Session()
base_url = 'http://rus.velohoster.com'

# 1. Fetch CSRF token from login page
login_url = f'{base_url}/accounts/login/'
resp = session.get(login_url)
print("Login page status:", resp.status_code)
csrf_token = session.cookies.get('csrftoken')

# 2. Login as driver
login_data = {
    'email': 'driver@topd.kg',
    'password': 'driver123',
    'csrfmiddlewaretoken': csrf_token
}
resp_login = session.post(login_url, data=login_data, headers={'Referer': login_url}, allow_redirects=True)
print("After login final URL:", resp_login.url, "Status:", resp_login.status_code)
assert '/dashboard/driver/' in resp_login.url, f"Expected /dashboard/driver/, got {resp_login.url}"

# 3. Test each driver menu page
pages = [
    ('/dashboard/driver/', 'Driver Profile & Performance'),
    ('/dashboard/driver/vehicle/', 'Current Assigned Vehicle'),
    ('/dashboard/driver/agreements/', 'Assigned Contract Records'),
    ('/dashboard/driver/history/', 'Incident & Violation History'),
]

for path, marker in pages:
    url = f'{base_url}{path}'
    r = session.get(url)
    print(f"Testing {url} -> Status: {r.status_code}")
    assert r.status_code == 200, f"Failed on {url}: status {r.status_code}"
    # Verify markers
    assert marker.lower() in r.text.lower(), f"Marker '{marker}' not found on {url}"
    # Check that sidebar links are separate URLs and not #active-car
    assert '/dashboard/driver/vehicle/' in r.text, f"Vehicle menu link not found on {url}"
    assert '/dashboard/driver/agreements/' in r.text, f"Agreements menu link not found on {url}"
    assert '/dashboard/driver/history/' in r.text, f"History menu link not found on {url}"
    print(f"  [OK] Found marker '{marker}' and sidebar navigation links!")

print("\nALL LIVE DRIVER MENU PAGES VERIFIED SUCCESSFULLY ON RUS.VELOHOSTER.COM!")
