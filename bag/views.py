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
    quantity_250g = int(request.POST.get('quantity_250g', 0))
    quantity_1kg = int(request.POST.get('quantity_1kg', 0))
    quantity_ac = int(request.POST.get('quantity_ac', 0))

    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in bag:
        # Check if the selected weight already exists in the bag
        if '250g' in bag[item_id]:
            bag[item_id]['250g'] += quantity_250g
            messages.success(request, f'Updated {product.name} (250g) quantity to {bag[item_id]["250g"]}')
        else:
            bag[item_id]['250g'] = quantity_250g
            messages.success(request, f'Added {product.name} (250g) to your bag')

        if '1kg' in bag[item_id]:
            bag[item_id]['1kg'] += quantity_1kg
            messages.success(request, f'Updated {product.name} (1kg) quantity to {bag[item_id]["1kg"]}')
        else:
            bag[item_id]['1kg'] = quantity_1kg
            messages.success(request, f'Added {product.name} (1kg) to your bag')

        if 'ac' in bag[item_id]:
            bag[item_id]['ac'] += quantity_ac
            messages.success(request, f'Updated {product.name} (ac) quantity to {bag[item_id]["ac"]}')
        else:
            bag[item_id]['ac'] = quantity_ac
            messages.success(request, f'Added {product.name} (ac) to your bag')

    else:
        bag[item_id] = {'250g': quantity_250g, '1kg': quantity_1kg, 'ac': quantity_ac}
        messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)



def adjust_bag(request, item_id):
    """View to allow users to make modifications to the current shopping bag"""

    product = get_object_or_404(id=item_id)

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')
    
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
