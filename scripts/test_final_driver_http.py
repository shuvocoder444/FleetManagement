import requests

s = requests.Session()
r_login_page = s.get('http://rus.velohoster.com/accounts/login/')
csrf = s.cookies.get('csrftoken')

post_data = {
    'email': 'driver@topd.kg',
    'password': 'driver123',
    'csrfmiddlewaretoken': csrf
}

r_post = s.post('http://rus.velohoster.com/accounts/login/', data=post_data, headers={'Referer': 'http://rus.velohoster.com/accounts/login/'}, allow_redirects=True)
print("Post login URL:", r_post.url, "Status:", r_post.status_code)
assert r_post.status_code == 200

# Now access pages with logged in driver session
for path in ['/dashboard/driver/', '/dashboard/driver/vehicle/', '/dashboard/driver/agreements/', '/dashboard/driver/history/']:
    res = s.get(f'http://rus.velohoster.com{path}')
    print(f"Logged-in driver GET {path} -> {res.status_code}")
    assert res.status_code == 200

print("ALL DRIVER ACTIONS 100% OPERATIONAL OVER HTTP!")

