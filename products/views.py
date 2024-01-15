from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category
from .forms import ProductForm

# Create your views here.

def all_products(request):
    """ This view show all products, including sorting and searches """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if sortkey == 'category':
                sorkey = 'category__name'

            if sortkey == 'price_ac_asc':
                sortkey = 'price_ac'
            elif sortkey == 'price_ac_desc':
                sortkey = '-price_ac'
            elif sortkey == 'price_250g_asc':
                sortkey = 'price_250g'
            elif sortkey == 'price_250g_desc':
                sortkey = '-price_250g'
            elif sortkey == 'rates_asc':
                sortkey = 'rates'
            elif sortkey == 'rates_desc':
                sortkey = '-rates'


            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if  'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 's' in request.GET:
            query = request.GET['s']
            if not query:
                messages.error(request, 'No text was typed on the search')
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(brand__icontains=query)
            products = products.filter(queries)
    
    current_sorting = f'{sort}_{direction}'
    
    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'sort': sort,
        'direction': direction,
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """ This view show the details of the product when user clicks on it """

    product = get_object_or_404(Product, id=product_id)
    
    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


def add_product(request):
    """Add products to the store"""
    form = ProductForm
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)