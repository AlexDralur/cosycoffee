from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Producer
from .forms import ProducerForm

def producers(request):
    """ This view returns the producers page """

    producers = Producer.objects.all()
    return render(request, 'producers/producers.html', {'producers': producers})


@login_required
def add_producer(request):
    """View to add a new producer"""

    if request.method == "POST":
        form = ProducerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producer added successfully')
            return redirect('producers')
        else:
            messages.error(request, 'An error occurred. Please check the form.')
    else:
        form = ProducerForm()
    
    return render(request, 'producers/add_producer.html', {'form': form})