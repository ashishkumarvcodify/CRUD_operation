from django.db import models

class crud(models.Model):
    fullname = models.CharField(max_length=50)
    phonenumber = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    zipcode = models.TextField(max_length=10)