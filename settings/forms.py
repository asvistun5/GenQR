from django import forms
from .models import Card

class CardForm(forms.ModelForm):
    class Meta:
        model = Card

        fields = ['num', 'end', 'cvv']

        widgets = {
            "num": forms.TextInput(attrs= {"class": "form-field", "placeholder": "Введіть свій номер картки"}),
            "end": forms.DateInput(attrs={"class": "form-field", "placeholder": "Тривалість підписки", "type": "date"}),
            "cvv": forms.TextInput(attrs= {"class": "form-field", "placeholder": "Введіть CVV код"}),
        }

        labels = {field: '' for field in fields}