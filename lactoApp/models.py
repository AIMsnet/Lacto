from django.db import models
from datetime import datetime,date
# Create your models here.
class Batch(models.Model):
    Batch_No    = models.IntegerField()
    collection_date =   models.DateField(default=datetime.now, blank=True)
    pasteurizing_date  =    models.DateField(null=True)
    select_type =  models.CharField(max_length=20, blank=True)
    batch_type         =    models.CharField(max_length=20, blank=True)
    doner_id_homo = models.BooleanField(blank=True)
    self_other  =   models.CharField(max_length=20, blank=True)
    exp_date    =   models.DateField(blank=True)
    Pasturing_process_id    =   models.CharField(max_length=10, blank=True) 
    content1    =   models.CharField(max_length=125, blank=True)

class Doner(models.Model):
    doner_id = models.CharField(max_length=10)
    f_name  =  models.CharField(max_length=20, null=False)
    l_name  =    models.CharField(max_length=20, null=True)
    address  =   models.CharField(max_length=50, null=True)
    age   =  models.IntegerField(blank=True, null=True)
    HBS_test_date  = models.DateField(blank=True, null=True)
    HIV_test_date  =  models.DateField(blank=True, null=True)
    screening_test_date  = models.DateField(blank=True, null=True)
    VRDL_test  =  models.BooleanField(blank=True, null=True)
    VRDL_test_date =  models.DateField(blank=True, null=True)
    last_child_birth_date  = models.DateField(null=True)
    consent  =  models.BooleanField(null=True)
    consent_date = models.DateField(null=True)

