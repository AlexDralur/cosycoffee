from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def bag_contents(request):
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        product = get_object_or_404(Product, id=item_id)
        if isinstance(item_data, dict):
            # Iterate over weights and quantities in the item_data dictionary
            for weight, quantity in item_data.items():
                # Convert quantity to int if needed (it should already be an int)
                if isinstance(quantity, str):
                    quantity = int(quantity)

                subtotal = 0
                if weight == '250g' and hasattr(product, 'price_250g') and product.price_250g is not None:
                    subtotal = quantity * product.price_250g
                elif weight == '1kg' and hasattr(product, 'price_1kg') and product.price_1kg is not None:
                    subtotal = quantity * product.price_1kg
                elif weight == 'ac' and hasattr(product, 'price_ac') and product.price_ac is not None:
                    subtotal = quantity * product.price_ac

                total += subtotal
                product_count += quantity

                bag_items.append({
                    'item_id': item_id,
                    'weight': weight,
                    'quantity': quantity,
                    'product': product,
                    'subtotal': subtotal,
                })
        else:
            weight = 'ac'  # Default weight if not specified
            quantity = item_data
            subtotal = quantity * product.price_ac

            total += subtotal
            product_count += quantity

            bag_items.append({
                'item_id': item_id,
                'weight': weight,
                'quantity': quantity,
                'product': product,
                'subtotal': subtotal,
            })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
