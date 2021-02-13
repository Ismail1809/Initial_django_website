from django.db import models

# Create your models here.

class Product(models.Model):
	login = models.CharField(max_length = 30)
	password = models.CharField(max_length = 30)