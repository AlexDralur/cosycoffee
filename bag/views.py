from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from products.models import Product


# Create your views here.

def view_bag(request):
    """A view to allow the user to see the bag"""
    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """View to allow user to add items to the shopping bag"""

    product = Product.objects.get(id=item_id)

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag')
    
    request.session['bag'] = bag
    return redirect(redirect_url)

def adjust_bag(request, item_id):
    """View to allow users to make modifications to the current shopping bag"""

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop(item_id)
    
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))

def remove_from_bag(request, item_id):
    """View to allow users to remove item from the bag"""

    try:
        if 'bag' not in request.session:
            request.session['bag'] = {}

        bag = request.session['bag']
        
        if item_id in list(bag.keys()):
            if not bag[item_id]:
                bag.pop(item_id)
        
        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)