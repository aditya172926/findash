from django import forms
from .models import StockCsvFiles

class StockQueryForm(forms.Form):
    start = forms.DateTimeField()
    end = forms.DateTimeField()
    ticker = forms.CharField()

class CsvFiles(forms.ModelForm):
    description = forms.Textarea()
    csv_file = forms.FileField()
    class Meta:
        model = StockCsvFiles
        fields = (
            'description',
            'csv_file'
        )