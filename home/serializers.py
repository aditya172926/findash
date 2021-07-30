from rest_framework import serializers
from .models import StockCsvFiles

class StockCsvSerializers(serializers.ModelSerializer):
    class Meta:
        model = StockCsvFiles
        fields = (
            'csv_file',
            'description'
        )