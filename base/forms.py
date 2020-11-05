from django import forms
from django.contrib.auth.models import User

from .models import Product


class ShareForm(forms.Form):
    uname = forms.CharField(max_length=100)