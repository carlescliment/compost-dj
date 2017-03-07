from django.http import HttpResponse
from django.shortcuts import render, redirect
from compost.forms import MeasurementForm
from compost.models import Measurement
from compost.services import RegisterMeasurement

def home(request):
    measurements = Measurement.objects.all
    return render(request, 'home.html', {'measurements': measurements})

def new_measurement(request):
    if request.method == 'POST':
        form = MeasurementForm(request.POST)
        if form.is_valid():
            RegisterMeasurement().execute(form.cleaned_data)
            return redirect('home')
    else:
        form = MeasurementForm()
    return render(request, 'measurements/add.html', {'form': form})
