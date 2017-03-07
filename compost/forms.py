from django import forms

class MeasurementForm(forms.Form):
    temperature = forms.FloatField(required=True)
