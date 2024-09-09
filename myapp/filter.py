import django_filters
from django import forms
from django_filters import CharFilter
from .models import product  # Adjust the import according to your project structure

class PlaceFilter(django_filters.FilterSet):
    brand = django_filters.CharFilter(
        label="",
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={
            'placeholder': 'Search brand',
            'class': 'form-control'
        })
    ),

    

   
    class Meta:
        model = product
        fields = ['brand',]  # Include both 'brand' and 'produtz'
