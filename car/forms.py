from django import forms

from car.models import Representation

class CarForm(forms.ModelForm):
    class Meta:
        model = Representation
        fields = ['province', 'agent_code', 'city', 'email', 'regional_office', 'managers_name', 'sales_areas']