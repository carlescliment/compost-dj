from django import forms

class MeasurementForm(forms.Form):
    temperature = forms.FloatField(required=True)

    def clean_temperature(self):
        temperature = self.cleaned_data['temperature']
        if temperature < -273.15:
            raise forms.ValidationError("Temperature can't be under absolute zero")
        return temperature
