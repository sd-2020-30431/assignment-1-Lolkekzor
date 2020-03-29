from django import forms

from .models import ListItem


class DateInput(forms.DateInput):
    input_type = 'date'


class ListItemForm(forms.ModelForm):
    class Meta:
        model = ListItem
        fields = ['name', 'quantity', 'calories', 'purchase_date', 'expiration_date', 'consumption_date']
        widgets = {
            'purchase_date': DateInput(),
            'expiration_date': DateInput(),
            'consumption_date': DateInput()
        }
