import urllib.request
import urllib.parse
import http.cookiejar

cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

# 1. GET login page
resp = opener.open('http://rus.velohoster.com/accounts/login/')
print('Login GET status:', resp.status)

# 2. POST login form
data = urllib.parse.urlencode({
    'email': 'driver@topd.kg',
    'password': 'driver123'
}).encode('utf-8')

req = urllib.request.Request('http://rus.velohoster.com/accounts/login/', data=data, method='POST')
try:
    resp2 = opener.open(req)
    print('Login POST final URL:', resp2.geturl())
    print('Login POST status:', resp2.status)
    content = resp2.read().decode('utf-8', errors='ignore')
    if 'Invalid email or password' in content:
        print('ERROR: "Invalid email or password" found in page!')
    else:
        print('SUCCESS: Logged in! Title snippet:', content[:500])
except Exception as e:
    print('Exception:', e)

