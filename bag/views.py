from django.shortcuts import render

# Create your views here.

def view_bag(request):
    """A view to allow the user to see the bag"""
    return render(request, 'bag/bag.html')