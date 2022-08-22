from django.http import HttpResponse
from django.shortcuts import render

from .models import Destination

# Create your views here.


def index(request):
    # dest1 = Destination()
    # dest1.name = 'Mumbai'
    # dest1.desc = 'Beautiful city'
    # dest1.img = 'destination_1.jpg'
    # dest1.price = 700
    # dest1.offer = True
    # dest2 = Destination()
    # dest2.name = 'Mumbai2'
    # dest2.desc = 'Beautiful city'
    # dest2.img = 'destination_2.jpg'
    # dest2.price = 600
    # dest2.offer = False
    # dest3 = Destination()
    # dest3.name = 'Mumbai3'
    # dest3.desc = 'Beautiful city'
    # dest3.img = 'destination_3.jpg'
    # dest3.price = 500
    # dest3.offer = True
    # dests = [dest1, dest2, dest3]
    dests = Destination.objects.all()
    # return HttpResponse("hello to world")
    # return render(request, 'index.html')
    return render(request, "index.html", {'dests': dests})
