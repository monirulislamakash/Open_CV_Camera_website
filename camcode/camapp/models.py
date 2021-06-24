from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class AddCamera(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    Name=models.CharField(max_length=50,default="")
    Password=models.CharField(max_length=50,default="")
    Ip_Adderss=models.CharField(max_length=50,default="")
    Camera_Number=models.CharField(max_length=50,default="")
    def __str__(self):
        return self.Name