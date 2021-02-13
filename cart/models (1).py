from django.db import models

# Create your models here.

class Product(models.Model):
	name = models.CharField(max_length = 30)
	image_link = models.CharField()
	price = models.IntegerField()
	producer = models.ForeignKey(Producer, on_delete = models.CASCADE) # Foreign key

	# CREATE TABLE products VALUES(name text, image_link text, price int)

class Producer(models.Model):
	name = models.CharField()
	products_type = models.CharField()


# Шоколад - Lindt



# Lindt