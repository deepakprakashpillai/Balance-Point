
from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()
class HydrationLog(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="hydration_logs",null=True,blank=True)
    amount=models.FloatField()
    timestamp=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user} drank {self.amount} L on {self.timestamp}"



# Create your models here.
