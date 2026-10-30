import requests

s = requests.Session()
base_url = 'http://rus.velohoster.com'

# 1. Switch to Russian
r_lang_ru = s.get(f'{base_url}/switch-language/ru/', allow_redirects=True)
print("Switched to RU status:", r_lang_ru.status_code)

# 2. Get purchase page in Russian
r_ru = s.get(f'{base_url}/billing/purchase/')
print("GET /billing/purchase/ in RU status:", r_ru.status_code)
html_ru = r_ru.content.decode('utf-8')

assert 'Оформление подписки' in html_ru, "RU title 'Оформление подписки' not found!"
assert 'Выберите ваш тариф' in html_ru, "RU plan title 'Выберите ваш тариф' not found!"
assert 'Инструкции по оплате' in html_ru, "RU instructions 'Инструкции по оплате' not found!"
assert 'Сумма к оплате' in html_ru, "RU payable 'Сумма к оплате' not found!"
assert 'Реквизиты для банковского перевода' in html_ru, "RU bank details not found!"
assert 'Способ оплаты' in html_ru, "RU method not found!"
assert 'Купить подписку' in html_ru, "RU menu 'Купить подписку' not found!"
print(" [OK] All Russian translation keys verified on live server!")

# 3. Switch to English
r_lang_en = s.get(f'{base_url}/switch-language/en/', allow_redirects=True)
print("Switched to EN status:", r_lang_en.status_code)

# 4. Get purchase page in English
r_en = s.get(f'{base_url}/billing/purchase/')
print("GET /billing/purchase/ in EN status:", r_en.status_code)
html_en = r_en.content.decode('utf-8')

assert 'Purchase Subscription' in html_en, "EN title 'Purchase Subscription' not found!"
assert 'Choose Your Plan' in html_en, "EN plan title 'Choose Your Plan' not found!"
assert 'Payment Instructions' in html_en, "EN instructions 'Payment Instructions' not found!"
assert 'Payable Amount' in html_en, "EN payable 'Payable Amount' not found!"
assert 'Buy Subscription' in html_en, "EN menu 'Buy Subscription' not found!"
print(" [OK] All English translation keys verified on live server!")

print("\nALL LIVE PURCHASE TRANSLATION TESTS PASSED 100%!")
