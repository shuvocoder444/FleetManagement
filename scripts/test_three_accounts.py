import requests
import sys

sys.stdout.reconfigure(encoding='utf-8')

base_url = 'http://rus.velohoster.com'

accounts = [
    {
        'role_name': 'Super Admin',
        'email': 'admin@topd.kg',
        'password': 'admin123',
        'expected_dashboard': '/dashboard/superadmin/',
        'test_links': ['/agreements/', '/vehicles/', '/drivers/', '/billing/subscriptions/', '/settings/']
    },
    {
        'role_name': 'Rental Agency',
        'email': 'company@topd.kg',
        'password': 'company123',
        'expected_dashboard': '/dashboard/admin/',
        'test_links': ['/vehicles/', '/agreements/', '/accounts/team/', '/billing/purchase/']
    },
    {
        'role_name': 'Driver',
        'email': 'driver@topd.kg',
        'password': 'driver123',
        'expected_dashboard': '/dashboard/driver/',
        'test_links': ['/dashboard/driver/vehicle/', '/dashboard/driver/agreements/', '/dashboard/driver/history/']
    }
]

for acc in accounts:
    print(f"\n==========================================")
    print(f"TESTING: {acc['role_name']} ({acc['email']})")
    print(f"==========================================")
    
    s = requests.Session()
    # 1. Get login page
    r_login = s.get(f'{base_url}/accounts/login/')
    csrf = s.cookies.get('csrftoken')
    
    # 2. Post login
    post_data = {
        'email': acc['email'],
        'password': acc['password'],
        'csrfmiddlewaretoken': csrf
    }
    r_post = s.post(f'{base_url}/accounts/login/', data=post_data, headers={'Referer': f'{base_url}/accounts/login/'}, allow_redirects=True)
    print(f"Login Response: Status {r_post.status_code}, Final URL: {r_post.url}")
    
    if acc['expected_dashboard'] not in r_post.url:
        print(f"❌ FAIL: Expected {acc['expected_dashboard']} but got {r_post.url}")
    else:
        print(f"✅ SUCCESS: Landed on {acc['expected_dashboard']}")
        
    # Check top navbar text on dashboard
    print(f"\nChecking top navbar on {r_post.url}:")
    if 'Fleet Admin' in r_post.text:
        print("⚠️ Warning: 'Fleet Admin' found in page!")
    else:
        print("✅ 'Fleet Admin' NOT found in page!")
        
    # 3. Test clicking menus
    for path in acc['test_links']:
        test_url = f"{base_url}{path}"
        r_menu = s.get(test_url)
        print(f"\nMenu: {path} -> Status: {r_menu.status_code}, Final URL: {r_menu.url}")
        html = r_menu.text
        
        if acc['role_name'] == 'Super Admin':
            if 'SUPER ADMIN SIDEBAR' in html:
                print(f"  ✅ Has Super Admin sidebar")
            else:
                print(f"  ❌ MISSING Super Admin sidebar!")
            if 'FLEET COMPANY ADMIN SIDEBAR' in html:
                print(f"  ❌ Mistakenly has Company Admin sidebar!")
            if '/dashboard/superadmin/' in html:
                print(f"  ✅ Has /dashboard/superadmin/ link")
            else:
                print(f"  ❌ Missing /dashboard/superadmin/ link")
                
        elif acc['role_name'] == 'Rental Agency':
            if 'FLEET COMPANY ADMIN SIDEBAR' in html:
                print(f"  ✅ Has Company Admin sidebar")
            else:
                print(f"  ❌ MISSING Company Admin sidebar!")
            if 'SUPER ADMIN SIDEBAR' in html:
                print(f"  ❌ Mistakenly has Super Admin sidebar!")
                
        elif acc['role_name'] == 'Driver':
            if 'DRIVER SIDEBAR' in html:
                print(f"  ✅ Has Driver sidebar")
            else:
                print(f"  ❌ MISSING Driver sidebar!")
                
    # 4. Test visiting public website while logged in
    r_home = s.get(f'{base_url}/')
    print(f"\nVisiting Homepage (/) while logged in:")
    print(f"  Homepage status: {r_home.status_code}")
    if 'Sign In' in r_home.text and 'Dashboard' not in r_home.text:
        print(f"  ❌ User appears logged out on homepage!")
    else:
        print(f"  ✅ User remains logged in on homepage (Dashboard button present)")
