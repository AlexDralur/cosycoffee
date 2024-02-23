from django.shortcuts import render

# Create your views here.


def index(request):
    """ This view returns the index page """
    return render(request, 'home/index.html')


def privacy(request):
    """ This view returns the privacy page """
    return render(request, 'home/privacy.html')


def view404(request, exception):
    """ This view returns the privacy page """
    return render(request, '404.html', status=404)