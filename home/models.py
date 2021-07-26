from django.db import models

# Create your models here.
class StockCsvFiles(models.Model):
    id = models.AutoField(primary_key=True)
    csv_file = models.FileField()
    description = models.TextField(default = '', blank=True)