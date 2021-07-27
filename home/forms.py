from django import forms
from .models import StockCsvFiles

class StockQueryForm(forms.Form):
    start = forms.DateTimeField()
    end = forms.DateTimeField()
    ticker = forms.CharField()

class CsvFiles(forms.ModelForm):
    csv_file = forms.FileField()
    description = forms.Textarea()
    class Meta:
        model = StockCsvFiles
        fields = (
            'csv_file',
            'description'
        )