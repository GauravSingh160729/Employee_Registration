from django.db import models

# Create your models here.

    
class user(models.Model):
    Name = models.CharField(max_length=70)
    Gender= models.CharField(max_length=50)
    Designation=models.CharField(max_length=100)
  
    

    