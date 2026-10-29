from django import template
from decimal import Decimal, InvalidOperation

register = template.Library()


@register.filter
def convert_currency(amount, active_currency=None):
    """
    Converts a base USD price to the target currency.
    If active_currency is KGS: price * exchange_rate (e.g. 29 * 87.45 = 2,536 сом)
    If active_currency is USD or None: $29
    """
    if amount is None or amount == '':
        return ''
    
    try:
        val = Decimal(str(amount))
    except (InvalidOperation, ValueError, TypeError):
        return amount

    if not active_currency:
        if val == val.to_integral():
            return f"${int(val):,}"
        return f"${val:,.2f}"

    rate = getattr(active_currency, 'exchange_rate', Decimal('1.0'))
    code = getattr(active_currency, 'code', 'USD')
    symbol = getattr(active_currency, 'symbol', '$')

    try:
        converted = val * Decimal(str(rate))
    except Exception:
        converted = val

    if code == 'USD':
        if converted == converted.to_integral():
            return f"${int(converted):,}"
        return f"${converted:,.2f}"
    elif code == 'KGS':
        disp_symbol = 'KGS'
        if converted >= 100:
            return f"{round(converted):,} {disp_symbol}"
        elif converted == converted.to_integral():
            return f"{int(converted):,} {disp_symbol}"
        else:
            return f"{converted:,.2f} {disp_symbol}"
    else:
        if converted == converted.to_integral():
            return f"{int(converted):,} {symbol}"
        return f"{converted:,.2f} {symbol}"


@register.simple_tag(takes_context=True)
def convert_price(context, amount):
    """
    Takes context directly and converts amount using context['active_currency'].
    Usage: {% convert_price plan.price %}
    """
    active_currency = context.get('active_currency')
    return convert_currency(amount, active_currency)


@register.filter
def currency_symbol(active_currency):
    if not active_currency:
        return '$'
    return getattr(active_currency, 'symbol', '$')
