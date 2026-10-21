from django import forms
from .models import Zone

class ZoneForm(forms.ModelForm):
    class Meta:
        model = Zone
        fields = ['title', 'subtitle', 'category', 'price', 'emoji', 'tag',
                  'popular', 'cpu', 'gpu', 'ram', 'monitor', 'features',
                  'description', 'is_active']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'emoji': forms.TextInput(attrs={'class': 'form-control'}),
            'tag': forms.TextInput(attrs={'class': 'form-control'}),
            'cpu': forms.TextInput(attrs={'class': 'form-control'}),
            'gpu': forms.TextInput(attrs={'class': 'form-control'}),
            'ram': forms.TextInput(attrs={'class': 'form-control'}),
            'monitor': forms.TextInput(attrs={'class': 'form-control'}),
            'features': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }