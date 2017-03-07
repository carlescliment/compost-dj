from django.http import HttpResponse
from django.shortcuts import render, redirect
from compost.models import Measurement
from compost.forms import MeasurementForm
import datetime

def home(request):
    measurements = Measurement.objects.all
    return render(request, 'home.html', {'measurements': measurements})

def new_measurement(request):
    if request.method == 'POST':
        form = MeasurementForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            now = datetime.datetime.now()
            Measurement.objects.create(temperature=cd['temperature'], taken_at=now)
            return redirect('home')
    else:
        form = MeasurementForm()
    return render(request, 'measurements/add.html', {'form': form})
