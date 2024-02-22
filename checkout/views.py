from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from . models import Order, OrderLineItem
from bag.contexts import bag_contents
from products.models import Product
from profiles.forms import UserProfileForm
from profiles.models import UserProfile

import stripe
import json

@require_POST
def cache_checkout_data(request):
    """Function to keep information in cache"""

    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment was not processed. \
            Sorry for the inconvenience. Please try again later.') 
        return HttpResponse(content=e, status=400)


def checkout(request):
    """Function connecting order to Stripe"""
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address_1': request.POST['street_address_1'],
            'street_address_2': request.POST['street_address_2'],
            'county': request.POST['county'],
        }

        order_form = OrderForm(form_data)

        if order_form.is_valid():
            order = order_form.save()
            for item_id, item_data in bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, dict):
                        for size, quantity in item_data.items():
                            order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            product_size=size,  # Save the product size
                            quantity=quantity,  # Save the quantity
                    )
                    order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products added to the bag was not found.")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your details. Please double check all the fields.')

    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, 'No items are currently in the bag')
            return redirect (reverse('products'))

        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )
        print(intent)
        order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    return render(request, template, context)

def checkout_success(request, order_number):
    """Handle successful checkouts"""
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

    # Save the user's info
    if save_info:
        profile_data = {
            'default_phone_number': order.phone_number,
            'default_postcode': order.postcode,
            'default_town_or_city': order.town_or_city,
            'default_street_address_1': order.street_address_1,
            'default_street_address_2': order.street_address_2,
            'default_county': order.county,
            'default_country': order.country,
        }
        user_profile_form = UserProfileForm(profile_data, instance=profile)
        if user_profile_form.is_valid():
            user_profile_form.save()

    messages.success(request, f'Order completed. Thank you for shopping with us. \
         You will receive a confirmation email soon. \
         Your order number is {order_number}')

    if 'bag' in request.session:
        bag = request.session['bag']
        bag_items = []
        for item_id, item_data in bag.items():
            product = get_object_or_404(Product, pk=item_id)
            for weight, quantity in item_data.items():
                subtotal = getattr(product, f'price_{weight}') * quantity
                bag_items.append({
                    'product': product,
                    'quantity': quantity,
                    'weight': weight,
                    'subtotal': subtotal
                })

        total = order.order_total
        delivery = order.delivery_cost
        grand_total = order.grand_total
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total if total < settings.FREE_DELIVERY_THRESHOLD else 0

        context = {
            'order': order,
            'bag_items': bag_items,
            'total': total,
            'delivery': delivery,
            'grand_total': grand_total,
            'free_delivery_delta': free_delivery_delta,
        }

        del request.session['bag']  # Clear the bag from session after checkout

        print(context)
        return render(request, 'checkout/checkout_success.html', context)
    else:
        messages.error(request, 'Bag not found in session.')
        return redirect(reverse('products'))