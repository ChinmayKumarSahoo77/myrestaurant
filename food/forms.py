from django import forms
from .models import Food

'''
We need to create a class in forms.py file for each form we create.

It tells django that here is the Model I'll use for this particular form and these are the
fields for which we'll accept the data/inputs from the user
'''
class CreateForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'description', 'price', 'image', 'isveg']