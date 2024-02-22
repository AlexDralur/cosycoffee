from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product


# Create your views here.

def view_bag(request):
    """A view to allow the user to see the bag"""
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """Add a quantity of the specified product to the shopping bag"""
    product = get_object_or_404(Product, id=item_id)

    # Determine which quantity input was submitted
    if 'quantity_250g' in request.POST and request.POST['quantity_250g'] != '0':
        quantity = int(request.POST['quantity_250g'])
        weight = '250g'
    elif 'quantity_1kg' in request.POST and request.POST['quantity_1kg'] != '0':
        quantity = int(request.POST['quantity_1kg'])
        weight = '1kg'
    elif 'quantity_ac' in request.POST and request.POST['quantity_ac'] != '0':
        quantity = int(request.POST['quantity_ac'])
        weight = 'ac'
    else:
        # Handle the case where none of the quantity inputs were submitted
        messages.error(request, "Invalid request.")
        return redirect(reverse('view_bag'))

    bag = request.session.get('bag', {})

    if item_id in bag:
        # If the item ID exists in the bag, update the quantity for the weight
        if weight in bag[item_id]:
            bag[item_id][weight] += quantity
        else:
            bag[item_id][weight] = quantity
    else:
        # If the item ID is not in the bag, add it with the quantity for the weight
        bag[item_id] = {weight: quantity}

    request.session['bag'] = bag
    messages.success(request, f"Added {quantity} of {product.name} ({weight}) to your bag.")
    print('bag', bag)
    # Redirect back to the referrer
    redirect_url = request.META.get('HTTP_REFERER', '/')
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""
    quantity = int(request.POST.get('quantity'))
    weight = request.POST.get('product_weight')

    bag = request.session.get('bag', {})

    if item_id in bag and weight in bag[item_id]:
        bag[item_id][weight] = quantity
    
    print('current bag', bag)
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))



def remove_from_bag(request, item_id, weight):
    """Remove the specified quantity of a weight from the shopping bag"""
    bag = request.session.get('bag', {})

    if item_id in bag and weight in bag[item_id]:
        # Reduce the quantity of the specified weight to 0
        bag[item_id][weight] = 0
        messages.success(request, f"Removed {weight} from the item in your bag.")
        # If the weight is now 0, delete it from the bag
        if bag[item_id][weight] == 0:
            del bag[item_id][weight]
        # If the item has no more weights, remove the item from the bag
        if not bag[item_id]:
            del bag[item_id]
    else:
        messages.error(request, f"Weight '{weight}' not found for the item or item not found in your bag.")

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))

