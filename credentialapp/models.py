from django.db import models

# Create your models here.

#Customer Registration Table
class reg_user(models.Model):
    email=models.CharField(max_length=200,unique=True)
    password = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    house_name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    pincode = models.CharField(max_length=200)
    phone_no = models.CharField(max_length=200)

    def __str__(self):
        return self.email

#Login Table
class log_user(models.Model):
     email= models.CharField(max_length=200,primary_key=True,unique=True)
     password = models.CharField(max_length=200)

