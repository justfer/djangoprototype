from django.db import models
from sequences import get_next_value 
# Create your models here.

class Account(models.Model):
    user_id = models.CharField(max_length=100)
    id_number = models.CharField(max_length=15)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)