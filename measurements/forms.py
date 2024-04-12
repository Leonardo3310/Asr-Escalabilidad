from django import forms
from .models import Measurement

class MeasurementForm(forms.ModelForm):
    class Meta:
        model = Measurement
        fields = [
            'variable',
            #'value',
            'description',
            'place',
            #'dateTime',
        ]

        labels = {
            'variable' : 'Variable',
            #'value' : 'Value',
            'description' : 'Description',
            'place' : 'Place',
            #'dateTime' : 'Date Time',
        }
