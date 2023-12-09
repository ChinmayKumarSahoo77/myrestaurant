from django import forms
from .models import Food


class CreateForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'description', 'price', 'image', 'is_veg']