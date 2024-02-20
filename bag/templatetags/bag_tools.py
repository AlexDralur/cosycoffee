from django import template

register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """Logic to calculate the subtotal of the bag"""
    return price * quantity