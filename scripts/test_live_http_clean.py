import requests

base_url = 'http://rus.velohoster.com'

test_urls = [
    '/',
    '/accounts/login/',
    '/dashboard/driver/',
    '/dashboard/driver/vehicle/',
    '/dashboard/driver/agreements/',
    '/dashboard/driver/history/',
]

for url_path in test_urls:
    url = f"{base_url}{url_path}"
    try:
        r = requests.get(url, timeout=15)
        print(f"GET {url} -> Status: {r.status_code}")
        if r.status_code != 200:
            print(f"Error content on {url}:", r.text[:300])
    except Exception as e:
        print(f"Exception requesting {url}:", e)

