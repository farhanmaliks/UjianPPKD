from django import forms
from .models import BukuTamu

class BukuTamuForm(forms.ModelForm):
    class Meta:
        model = BukuTamu
        fields = ['nama', 'email', 'pesan',]