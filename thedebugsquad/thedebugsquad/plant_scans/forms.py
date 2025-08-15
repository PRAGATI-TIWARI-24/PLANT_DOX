from django import forms
from .models import PlantScan

class PlantScanForm(forms.ModelForm):
    class Meta:
        model = PlantScan
        fields = ['title', 'description', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Provide any details about the plant condition...'}),
        } 