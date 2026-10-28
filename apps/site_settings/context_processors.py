from .models import WebsiteSetting, Currency


def site_settings_processor(request):
    try:
        setting = WebsiteSetting.load()
        currencies = Currency.objects.filter(is_active=True)
    except Exception:
        setting = None
        currencies = []
    
    current_currency = request.session.get('currency', 'KGS')

    return {
        'site_setting': setting,
        'currencies': currencies,
        'current_currency': current_currency,
    }

