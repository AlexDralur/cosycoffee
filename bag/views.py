from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product


# Create your views here.

def view_bag(request):
    """A view to allow the user to see the bag"""
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """View to allow user to add items to the shopping bag"""

    product = get_object_or_404(Product, id=item_id)

    # Get the selected weight from the POST data
    selected_weight = request.POST.get('product_weight')
    quantity = int(request.POST.get(f'quantity_{selected_weight}', 0))

    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in bag:
        # Check if the selected weight already exists in the bag
        if selected_weight in bag[item_id]:
            bag[item_id][selected_weight] += quantity
        else:
            bag[item_id][selected_weight] = quantity

        messages.success(request, f'Updated {product.name} ({selected_weight}) quantity to {bag[item_id][selected_weight]}')
    else:
        if selected_weight is None:
            selected_weight = 'ac'
            quantity = int(request.POST.get('quantity_ac', 0))
        bag[item_id] = {selected_weight: quantity}
        messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    print(bag)
    return redirect(redirect_url)



def adjust_bag(request, item_id):
    """View to allow users to make modifications to the current shopping bag including item size"""

    product = get_object_or_404(Product, id=item_id)
    quantity = int(request.POST.get('quantity'))
    item_size = request.POST.get('item_size')  # Get the item size from the POST request

    bag = request.session.get('bag', {})

    if item_id in bag:
        if quantity > 0:
            # Check if the item_id already has a nested dictionary for sizes
            if isinstance(bag[item_id], dict):
                bag[item_id][item_size] = quantity
            else:
                # This case handles the transition from a previous structure
                # where item_id may not have been a dict. Adjust as needed.
                bag[item_id] = {item_size: quantity}
            messages.success(request, f'Updated {product.name} ({item_size}) quantity to {bag[item_id][item_size]}')
        else:
            # Remove the size entry. If no sizes left, remove the item entirely.
            if item_size in bag[item_id]:
                bag[item_id].pop(item_size)
                if not bag[item_id]:
                    bag.pop(item_id)
                messages.success(request, f'Removed {product.name} ({item_size}) from your bag')
    else:
        # If the item_id is not in the bag, add it with the item_size and quantity
        bag[item_id] = {item_size: quantity}
        messages.success(request, f'Added {product.name} ({item_size}) to your bag with quantity {quantity}')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """View to allow users to remove item from the bag"""

    product = get_object_or_404(Product, id=item_id)

    try:
        if 'bag' not in request.session:
            request.session['bag'] = {}

        bag = request.session['bag']
        
        if item_id in bag:
            # Check if any quantity exists for the item
            if any(bag[item_id].values()):
                # Remove the item from the bag
                bag.pop(item_id)
                messages.success(request, f'Removed {product.name} from your bag')
            else:
                messages.warning(request, f'No quantity found for {product.name} in your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
