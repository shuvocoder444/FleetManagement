from .models import WebsiteSetting, Currency
from .translations import get_translation


def site_settings_processor(request):
    try:
        setting = WebsiteSetting.load()
        currencies = Currency.objects.filter(is_active=True)
    except Exception:
        setting = None
        currencies = []
    
    # 1. Determine active language (session -> cookie -> default 'en')
    current_lang = request.session.get('_language') or request.COOKIES.get('django_language') or 'en'
    if current_lang not in ['en', 'ru']:
        current_lang = 'en'

    # 2. Determine active currency
    current_currency = request.session.get('currency', 'KGS')

    return {
        'site_setting': setting,
        'currencies': currencies,
        'current_currency': current_currency,
        'current_lang': current_lang,
        't': get_translation(current_lang),
    }
