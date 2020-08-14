from django import forms
from .models import *
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        #exclude = ('name',) ~ ['name']
        #fields = ('code') ~ ['code']