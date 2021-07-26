from django.contrib import admin
from .models import StockCsvFiles
# Register your models here.

class StockCsvAdmin(admin.ModelAdmin):
    list_display = (
        'description',
        'csv_file'
    )

admin.site.register(StockCsvFiles, StockCsvAdmin)