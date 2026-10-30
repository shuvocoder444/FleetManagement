import requests

s = requests.Session()
base_url = 'http://rus.velohoster.com'

# 1. Login as company
r_login_page = s.get(f'{base_url}/accounts/login/')
csrf = s.cookies.get('csrftoken')

post_data = {
    'email': 'driver@topd.kg',
    'password': 'driver123',
    'csrfmiddlewaretoken': csrf
}

r_login = s.post(f'{base_url}/accounts/login/', data=post_data, headers={'Referer': f'{base_url}/accounts/login/'}, allow_redirects=True)
print("Login final URL:", r_login.url, "Status:", r_login.status_code)
print("Session cookies after login:", s.cookies.get_dict())

# 2. Visit homepage /
r_home = s.get(f'{base_url}/')
print("Homepage status:", r_home.status_code)
html_home = r_home.text

# Check if homepage shows logged in state or Sign In
has_dashboard = 'dashboard' in html_home.lower()
has_signin = 'sign in' in html_home.lower() or 'логин' in html_home.lower() or 'войти' in html_home.lower()
has_register = 'register' in html_home.lower() or 'регистрация' in html_home.lower()

print(f"Homepage checks: has_dashboard={has_dashboard}, has_signin={has_signin}, has_register={has_register}")

# Let's inspect the navbar HTML on homepage
start_idx = html_home.find('Action Buttons & Tools')
if start_idx != -1:
    print("\nNavbar Action Buttons HTML:")
    print(html_home[start_idx:start_idx+1500])
else:
    print("Action Buttons & Tools not found in HTML!")
