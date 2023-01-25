from django.shortcuts import render
from hotel.models import Hotel
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def reservar (request):
    hoteles=Hotel.objects.all()
    return render(request, "hoteles.html", {"hotel": hoteles})



    