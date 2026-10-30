import urllib.request
import urllib.parse
import http.cookiejar

cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

# 1. First visit company admin as unauthenticated / old session to get cookies
opener.open('http://rus.velohoster.com/dashboard/admin/')

# 2. Login as driver@topd.kg
data = urllib.parse.urlencode({
    'email': 'driver@topd.kg',
    'password': 'driver123'
}).encode('utf-8')

req = urllib.request.Request('http://rus.velohoster.com/accounts/login/?next=/dashboard/admin/', data=data, method='POST')
resp = opener.open(req)
final_url = resp.geturl()
print('Actual Browser Login Final URL:', final_url)
assert '/dashboard/driver/' in final_url, f"Expected driver dashboard, got {final_url}"

# 3. Now try to visit /dashboard/admin/ in this session
resp2 = opener.open('http://rus.velohoster.com/dashboard/admin/')
print('Attempt to visit /dashboard/admin/ redirected to:', resp2.geturl())
assert '/dashboard/driver/' in resp2.geturl()

print('SUCCESS! Real external HTTP test verified.')

