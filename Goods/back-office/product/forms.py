from django import forms
from Goods.models import ProductEnter

class ProductEnterForm(forms.ModelForm):
    class Meta:
        model = ProductEnter
        fields = ['product', 'quantity', 'date', 'description']
        widgets = {
            'product': forms.Select(attrs={
                'class': 'form-select',
                'aria-label': 'Select product'
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter quantity'
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Enter description'
            }),
        }
