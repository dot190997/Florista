from django import forms
from .models import Flower


class flowerform(forms.ModelForm):
    class Meta:
        model = Flower
        fields = ['flower_image']
