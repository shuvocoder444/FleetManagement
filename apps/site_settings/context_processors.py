from .models import WebsiteSetting, Currency
from .translations import get_translation


def site_settings_processor(request):
    try:
        setting = WebsiteSetting.load()
        currencies = list(Currency.objects.filter(is_active=True).order_by('-is_base', 'code'))
        if not currencies:
            usd, _ = Currency.objects.get_or_create(code='USD', defaults={'name': 'US Dollar', 'symbol': '$', 'exchange_rate': 1.0, 'is_base': True, 'is_active': True})
            kgs, _ = Currency.objects.get_or_create(code='KGS', defaults={'name': 'Kyrgyzstani Som', 'symbol': 'сом', 'exchange_rate': 87.45, 'is_base': False, 'is_active': True})
            currencies = [usd, kgs]
    except Exception:
        setting = None
        currencies = []
    
    # 1. Determine active language (session -> cookie -> default 'en')
    current_lang = request.session.get('_language') or request.COOKIES.get('django_language') or 'en'
    if current_lang not in ['en', 'ru']:
        current_lang = 'en'

    # 2. Determine active currency (session -> cookie -> default 'USD')
    current_currency = request.session.get('currency') or request.COOKIES.get('user_currency') or 'USD'
    current_currency = current_currency.upper()

    active_currency = None
    for c in currencies:
        if c.code == current_currency:
            active_currency = c
            break
    if not active_currency and currencies:
        active_currency = currencies[0]
        current_currency = active_currency.code

    return {
        'site_setting': setting,
        'currencies': currencies,
        'current_currency': current_currency,
        'active_currency': active_currency,
        'current_lang': current_lang,
        't': get_translation(current_lang),
    }
