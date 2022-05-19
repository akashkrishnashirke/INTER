from django.db import models

# Create your models here.

class account(models.Model):
    ID=models.IntegerField(primary_key=True)
    First_Name=models.CharField(max_length=30)
    Middle_Name=models.CharField(max_length=30)
    Last_name=models.CharField(max_length=30)
    Date_of_Birth=models.DateField()
    Age=models.IntegerField()
    Email=models.EmailField(max_length=100)
    AdharCard=models.IntegerField()

