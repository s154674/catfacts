from django.shortcuts import render
import random
#from django.http import HttpResponse
from .models import Catfact
# Create your views here.


def index(request):
    # Fetch catfacts, scramble and take 10
    catfacts = Catfact.objects.all().order_by('?')[:10]

    context = {
        'title': 'Here are 10 random cat facts',
        'catfacts': catfacts
    }

    return render(request, 'cats/index.html', context)
