from django import forms
from .models import *

class student_form(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    # emailid = forms.EmailField(widget=forms.EmailField( is_hidden=False ), required=True, max_length=100)
    contact_no = forms.CharField(widget=forms.NumberInput(), required=True, max_length=10)
    # city = forms.CharField(widget=forms.TextInput(),required=False, max_length=100)
    # marks = forms.CharField(widget=forms.NumberInput(),required=True, max_length=10)
