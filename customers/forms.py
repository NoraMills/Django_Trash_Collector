from django import forms
from .models import Customer


class customer_forms(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'zip_code',
                  'sus_start', 'sus_end',)


class change_pickup_form(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'reg_pickup', 'one_time_pickup',)
