from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category

# Create your views here.

def all_products(request):
    """ This view show all products, including sorting and searches """

    products = Product.objects.all()
    query = None
    categories = None

    if request.GET:
        if  'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 's' in request.GET:
            query = request.GET['s']
            if not query:
                message.error(request, 'No text was typed on the search')
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(brand__icontains=query)
            products = products.filter(queries)
    
    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """ This view show the details of the product when user clicks on it """

    product = get_object_or_404(Product, id=product_id)
    
    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)