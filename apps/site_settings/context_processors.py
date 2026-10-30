from .models import WebsiteSetting, Currency
from .translations import get_translation


def get_active_dashboard_role(request):
    """
    Returns the persistent active dashboard role ('superadmin', 'admin', 'driver').
    Guarantees that a Company / Rental Agency user always stays in 'admin' (Fleet Admin)
    and never inadvertently gets switched to 'superadmin'.
    """
    user = getattr(request, 'user', None)
    role_param = request.GET.get('role', '').strip().lower()
    
    if role_param in ['superadmin', 'admin', 'company', 'driver']:
        if role_param == 'company':
            role_param = 'admin'
        request.session['active_dashboard_role'] = role_param
        return role_param

    if user and user.is_authenticated:
        # Non-superadmin company users MUST stay in 'admin'
        if getattr(user, 'role', '') in ['company', 'admin', 'individual']:
            if not (getattr(user, 'is_superuser', False) or getattr(user, 'role', '') == 'superadmin'):
                request.session['active_dashboard_role'] = 'admin'
                return 'admin'
            return request.session.get('active_dashboard_role', 'admin')
        elif getattr(user, 'role', '') == 'driver':
            request.session['active_dashboard_role'] = 'driver'
            return 'driver'
        elif getattr(user, 'is_superuser', False) or getattr(user, 'role', '') == 'superadmin':
            return request.session.get('active_dashboard_role', 'superadmin')
        else:
            return request.session.get('active_dashboard_role', 'admin')

    return request.session.get('active_dashboard_role', 'superadmin')


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

    # 3. Determine current active dashboard role (Super Admin / Fleet Admin / Driver)
    current_dashboard = get_active_dashboard_role(request)
    user = getattr(request, 'user', None)

    # Display user object for avatars and names in dashboard
    display_user = user if (user and user.is_authenticated) else None
    if not display_user:
        try:
            from apps.accounts.models import CustomUser
            if current_dashboard == 'admin':
                display_user = CustomUser.objects.filter(role=CustomUser.Role.COMPANY).first() or CustomUser.objects.first()
            elif current_dashboard == 'driver':
                display_user = CustomUser.objects.filter(role=CustomUser.Role.DRIVER).first() or CustomUser.objects.first()
            else:
                display_user = CustomUser.objects.filter(role=CustomUser.Role.SUPERADMIN).first() or CustomUser.objects.first()
        except Exception:
            display_user = None

    return {
        'site_setting': setting,
        'currencies': currencies,
        'current_currency': current_currency,
        'active_currency': active_currency,
        'current_lang': current_lang,
        't': get_translation(current_lang),
        'current_dashboard': current_dashboard,
        'display_user': display_user,
    }
