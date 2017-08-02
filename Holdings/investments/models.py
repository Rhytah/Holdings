from django.db import models

from django.db import models

from django.utils import timezone

import datetime
now = timezone.now()

class Item(models.Model):
	item_name= models.CharField(max_length=30)
	item_id= models.IntegerField(primary_key = True, default=0)
	item_category = models.CharField(max_length=20)
	item_description= models.CharField(max_length=200)
	release_date = models.DateTimeField( null=True, blank = True,default = '')
	hardware = models.CharField(max_length=30, default='')

class Service(models.Model):
    service_name= models.CharField(max_length=20, default='')
    service_category = models.CharField(max_length=200)
    hardware = models.ForeignKey(Item, on_delete = models.CASCADE)
    description = models.TextField(null=True, blank = True)

class Look(models.Model):
    item_name= models.ForeignKey(Item, on_delete = models.CASCADE)
    Service = models.ForeignKey(Service, on_delete = models.CASCADE)
    gallery_item = models.ImageField(upload_to='img/photo')
    particular = models.CharField(max_length=30)
# Create your models here.
