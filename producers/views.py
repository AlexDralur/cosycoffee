from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Producer
from .forms import ProducerForm


def producers(request):
    """ This view returns the producers page """

    producers = Producer.objects.all()
    return render(
        request, 'producers/producers.html', {'producers': producers})


@login_required
def add_producer(request):
    """View to add a new producer"""

    if not request.user.is_superuser:
        messages.error(request, 'Access not permitted.')
        return redirect(reverse('producers'))

    if request.method == "POST":
        form = ProducerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producer added successfully')
            return redirect('producers')
        else:
            messages.error(
                request, 'An error occurred. Please check the form.')
    else:
        form = ProducerForm()
    return render(request, 'producers/add_producer.html', {'form': form})


@login_required
def edit_producer(request, producer_id):
    """View to edit an existing producer"""

    if not request.user.is_superuser:
        messages.error(request, 'Access not permitted.')
        return redirect('producers')

    producer = get_object_or_404(Producer, id=producer_id)
    if request.method == 'POST':
        form = ProducerForm(request.POST, request.FILES, instance=producer)
        if form.is_valid():
            form.save()
            messages.success(request, "Producer updated successfully!")
            return (redirect('producers'))
        else:
            messages.error(request, 'Failed to update producer. \
            Please check the form.')
    else:
        form = ProducerForm(instance=producer)
        messages.info(request, f'You are editing {producer.name}')

    template = 'producers/edit_producer.html'
    context = {
        'form': form,
        'producer': producer,
    }

    return render(request, template, context)


@login_required
def delete_producer(request, producer_id):
    """Delete a specific producer"""
    if not request.user.is_superuser:
        messages.error(request, 'Access not permitted.')
        return redirect(reverse('home'))

    producer = get_object_or_404(Producer, id=producer_id)
    producer.delete()
    messages.success(request, 'Producer deleted!')
    return redirect('producers')