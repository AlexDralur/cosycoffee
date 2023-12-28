from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Product

# Create your views here.

def all_products(request):
    """ This view show all products, including sorting and searches """

    products = Product.objects.all()

    if request.GET:
        if 's' in request.GET:
            query = request.GET['s']
            if not query:
                message.error(request, 'No text was typed on the search')
                return redirect(reverse('products'))
    
    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """ This view show the details of the product when user clicks on it """

    product = get_object_or_404(Product, id=product_id)
    
    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)