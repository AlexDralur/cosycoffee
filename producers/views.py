from django.shortcuts import render


def producers(request):
    """ This view returns the producers page """
    return render(request, 'producers/producers.html')