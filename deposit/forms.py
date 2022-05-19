from django import forms
from .models import deposit_model
class depaositForm(forms.ModelForm):
    class Meta:
        model=deposit_model
        fields="__all__"


