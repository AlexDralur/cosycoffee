from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, 'No items are currently in the bag')
        return redirect (reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51OTCoZGb2Fr8dq7QAxjSMltMkQDcXx1YKyiTrDzvAyMaEmdR1tmc93JSEyDdAyeUCzMHQqwcB2BrXdGGdY6Vvbgd00V92M5R46',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)