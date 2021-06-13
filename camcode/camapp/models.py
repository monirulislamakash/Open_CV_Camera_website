from django.db import models

# Create your models here.
class AddCamera(models.Model):
    Name=models.CharField(max_length=50)
    Password=models.CharField(max_length=50)
    Ip_Adderss=models.CharField(max_length=50)
    Camera_Number=models.CharField(max_length=50)
    def __str__(self):
        return self.Name