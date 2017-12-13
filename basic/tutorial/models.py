from django.db import models
# Create your models here.

class Account(models.Model):
    user_id = models.CharField(max_length=100)
    id_number = models.CharField(max_length=15)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)

    def __str__(self):
        return self.id_number + ' ' + self.first_name + ' ' + self.last_name


ASSETS_TYPES = (
    ('1','IT Equipment'),
    ('2','CISCO Equipment'),
    ('3','Computer Peripheral'),
    ('0','Other Equipment')
)

class TangibleAssets(models.Model):
    model_no = models.CharField(max_length=120)
    serial_no = models.CharField(max_length=120)
    termination_date = models.DateField() #dae ko aram ano parameters kani
    asset_type = models.CharField(choices=ASSETS_TYPES,max_length=1)