from django.db import models

# Create your models here.

class deposit_model(models.Model):
    ID=models.IntegerField(primary_key=True)
    First_Name = models.CharField(max_length=30)
    Middle_Name = models.CharField(max_length=30)
    Last_name = models.CharField(max_length=30)
    Email = models.EmailField(max_length=100)
    Deposit=models.IntegerField()

