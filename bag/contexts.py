from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def bag_contents(request):
    """Function to handle any changes within the bag
    and to adjust the subtotal accordingly"""
    
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        product = get_object_or_404(Product, id=item_id)
        subtotal = 0

        if isinstance(item_data, dict):
            for selected_weight, quantity in item_data.items():
                if selected_weight == '250g' and hasattr(product, 'price_250g') and product.price_250g is not None:
                    subtotal = quantity * product.price_250g
                elif selected_weight == '1kg' and hasattr(product, 'price_1kg') and product.price_1kg is not None:
                    subtotal = quantity * product.price_1kg
                elif selected_weight == 'ac' and hasattr(product, 'price_ac') and product.price_ac is not None:
                    subtotal = quantity * product.price_ac
                else:
                    subtotal = 0  # Handle other cases if needed
                
                total += subtotal
                product_count += quantity

                bag_items.append({
                    'item_id': item_id,
                    'weight': selected_weight,
                    'quantity': quantity,
                    'quantity_250g': quantity if selected_weight == '250g' else 0,
                    'quantity_1kg': quantity if selected_weight == '1kg' else 0,
                    'quantity_ac': quantity if selected_weight == 'ac' else 0,
                    'product': product,
                    'subtotal': subtotal,
                })
        else:
            selected_weight = 'ac'
            quantity = item_data
            subtotal += quantity * product.price_ac

            total += subtotal
            product_count += quantity

            bag_items.append({
                'item_id': item_id,
                'weight': selected_weight,
                'quantity': quantity,
                'quantity_250g': quantity if selected_weight == '250g' else 0,
                'quantity_1kg': quantity if selected_weight == '1kg' else 0,
                'quantity_ac': quantity if selected_weight == 'ac' else 0,
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
