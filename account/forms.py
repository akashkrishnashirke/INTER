from django import forms
from .models import account
from django.utils.version import get_version_tuple
class employee(forms.ModelForm):
    class Meta:
        model=account
        fields="__all__"


