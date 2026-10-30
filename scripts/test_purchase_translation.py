import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import django
django.setup()

from django.test import Client

client = Client()

# 1. Test in English
client.get('/switch-language/en/')
res_en = client.get('/billing/purchase/')
print("EN status:", res_en.status_code)
html_en = res_en.content.decode('utf-8')
assert 'Purchase Subscription' in html_en
assert 'Choose Your Plan' in html_en
assert 'Payment Instructions' in html_en
assert 'Payable Amount' in html_en

# 2. Test in Russian
client.get('/switch-language/ru/')
res_ru = client.get('/billing/purchase/')
print("RU status:", res_ru.status_code)
html_ru = res_ru.content.decode('utf-8')

# Check Russian strings
assert 'Оформление подписки' in html_ru, "Russian title not found!"
assert 'Выберите ваш тариф' in html_ru, "Russian choose plan not found!"
assert 'Инструкции по оплате' in html_ru, "Russian instructions not found!"
assert 'Сумма к оплате' in html_ru, "Russian payable amount not found!"
assert 'Купить подписку' in html_ru, "Russian buy subscription menu not found!"

print("ALL EN AND RU TESTS PASSED LOCALLY 100%!")
