import requests
import re

session = requests.Session()
r_get = session.get('http://rus.velohoster.com/accounts/login/')
print('GET status:', r_get.status_code)
csrf_cookie = session.cookies.get('csrftoken')
print('CSRF cookie from session:', csrf_cookie)

match = re.search(r'name=["\']csrfmiddlewaretoken["\'] value=["\']([^"\']+)["\']', r_get.text)
csrf_token_val = match.group(1) if match else None
print('CSRF token in form:', csrf_token_val)

payload = {
    'csrfmiddlewaretoken': csrf_token_val,
    'email': 'admin@topd.kg',
    'password': 'admin123',
}
headers = {
    'Referer': 'http://rus.velohoster.com/accounts/login/',
    'Origin': 'http://rus.velohoster.com',
}
r_post = session.post('http://rus.velohoster.com/accounts/login/', data=payload, headers=headers, allow_redirects=False)
print('POST status:', r_post.status_code)
if r_post.status_code == 302:
    print('SUCCESS! Redirect URL:', r_post.headers.get('Location'))
else:
    print('Failed response:', r_post.text[:400])

