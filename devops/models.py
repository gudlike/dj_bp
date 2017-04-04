from django.db import models

# Create your models here.
from django.db import models

class Runtime(models.Model):
    ip = models.CharField(max_length=64)
    monion_id = models.CharField(max_length=256)
    update_date = models.DateTimeField('date updated')

class Container(models.Model):
    name = models.CharField(max_length=256)