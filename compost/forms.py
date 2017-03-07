from django import forms

class MeasurementForm(forms.Form):
    ABSOLUTE_ZERO = -273.15

    temperature = forms.FloatField(required=True)

    def clean_temperature(self):
        temperature = self.cleaned_data['temperature']
        if temperature < self.ABSOLUTE_ZERO:
            raise forms.ValidationError("Temperature can't be under absolute zero")
        return temperature
