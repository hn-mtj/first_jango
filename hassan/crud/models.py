from django.db import models

# Create your models here.

import datetime
from django.utils import timezone

class Crud(models.Model):
    purchase = models.CharField(max_length=150)
    purchase_id = models.IntegerField()
    user_id = models.IntegerField()
    name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=200)
    address = models.TextField()
    date_time = models.DateTimeField('date published')
    
    #def __str__(self):
    #    return '%s %s %s %s %s' % (self.purchase, self.name, self.phone_number, self.email, self.address)

    #def was_published_recently(self):
    #    return self.date_time >= timezone.now() - datetime.timedelta(days=1)