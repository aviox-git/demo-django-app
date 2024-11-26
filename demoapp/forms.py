from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'dob', 'mobile', 'email']
        widgets = {
            'dob': forms.DateInput(attrs={'class': 'datepicker'})
        }
