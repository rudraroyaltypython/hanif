from django.db import models

# Create your models here.
class MacPrice(models.Model):
    wholesale = models.CharField(max_length=50,verbose_name='Mackerel (बांगडा) Wholesale Price per kg')
    

class KingPrice(models.Model):
    wholesale = models.CharField(max_length=50,verbose_name='King Fish (सुरमई) Wholesale Price per kg')

class PrawnsPrice(models.Model):
    wholesale = models.CharField(max_length=50,verbose_name='Prawns (कोळंबी) Wholesale Price per kg')