from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Producer

def producers(request):
    """ This view returns the producers page """

    producers = Producer.objects.all()
    return render(request, 'producers/producers.html', {'producers': producers})