from django import template

register = template.Library()


@register.filter
def divide(value, divisor):
    try:
        return float(value) / float(divisor)
    except (ValueError, ZeroDivisionError):
        return 0.0


@register.filter
def price_convertor(value):
    price = str(value)
    if len(price) == 7:
        np = price[:2]
        price = np + ' Lakhs'
        return price
    if len(price) == 8:
        np = price[:2]
        price = np + ' Cr.'
        return price
# def abcde():
#     pass