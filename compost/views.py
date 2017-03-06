from django.http import HttpResponse
from django.shortcuts import render, redirect
from compost.models import Measurement
import datetime

def home(request):
    now = datetime.datetime.now()
    return render(request, 'home.html', {'now': now})

def new_measurement(request):
    return render(request, 'measurements/add.html')

def create_measurement(request):
    now = datetime.datetime.now()
    Measurement.objects.create(temperature=request.GET['temperature'], taken_at=now)

    return redirect('home')
