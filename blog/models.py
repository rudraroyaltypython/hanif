from django.db import models


# Create your models here.
class Para(models.Model):
    title_test = models.CharField(max_length=50)
    info_test =  models.CharField(max_length=50)

