from django.shortcuts import render
from .models import Producer


def producers(request):
    """ This view returns the producers page """

    model = Producer
    
    return render(request, 'producers/producers.html')