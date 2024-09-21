from django_filters import FilterSet, CharFilter
from django import forms
from django.db.models import Q
from .models import product

class PlaceFilter(FilterSet):
    search = CharFilter(
        label="Search",
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={
            'placeholder': 'Search for brand, name, or specifications...',
            'class': 'form-control',
            'onfocus': "this.value=''"  # Optional: Clear on focus
        })
    )

    class Meta:
        model = product
        fields = []

    def filter_queryset(self, queryset):
        search = self.data.get('search')
        if search:
            queryset = queryset.filter(
                Q(brand__icontains=search) |
                Q(name__icontains=search) |
                Q(specification__icontains=search) |
                Q(price__icontains=search)
            )
        return queryset
