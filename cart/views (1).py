from django.shortcuts import render
from django.http import HttpResponse

from . import models

# Create your views here.

def catalog_home(request):
	data = {
		"name": "Chocolate",
		"image_link": "/img/choclate.png",
		"price": 100,
	}

	prod = models.Product(data["name"], data["image_link"], data["price"])
	prod.save()

	# Get data

	products = models.Product.objects.all()

	products_filtered = models.Product.filter(members__price__gt = 60) # gt - greater than, больше чем

	# return HttpResponse("Hello from Django app!")

	return render(request, "/catalog/catalog.html", data = products)


'''

<ul>
{% for prod in data %}
	<li>Name: prod.name</li>
	
{% endfor %}
</ul>

'''