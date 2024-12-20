from django.db import models
from django.contrib.auth import get_user_model
from datetime import timedelta

User=get_user_model()

class SleepLog(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='sleep_logs',null=True,blank=True)
    sleep_start=models.DateTimeField()
    sleep_end=models.DateTimeField()
    duration=models.DurationField(null=True,blank=True)
    quality=models.IntegerField(choices=[(1,'very poor'),(2,'poor'),(3,'fair'),(4,'good'),(5,'very good')],default='3')
    interrupted=models.BooleanField(default=False)









# Create your models here.
