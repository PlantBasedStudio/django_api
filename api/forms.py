from django import forms
from base.models import Products

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'