from django import forms
from .models import Menu

class AddForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['item','price','description','item_image']