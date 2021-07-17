from django import forms
from django.forms import fields

class StockQueryForm(forms.Form):
    start = forms.DateTimeField()
    end = forms.DateTimeField()
    ticker = forms.CharField()