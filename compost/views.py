from django.http import HttpResponse
from django.shortcuts import render, redirect
import datetime

def home(request):
    now = datetime.datetime.now()
    return render(request, 'home.html', {'now': now})

def new_measurement(request):
    return render(request, 'measurements/add.html')

def create_measurement(request):
    return redirect('home')
