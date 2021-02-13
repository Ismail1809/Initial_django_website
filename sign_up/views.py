from django.shortcuts import render, redirect

from . import forms

from . import models
# Create your views here.

def sign_up_page(request):
	if request.method == "POST":
		form = forms.SignUp(request.POST)

		print("Form is correct: ", form.is_valid())

		print(request.POST)

		if form.is_valid():
			data = {
				"login": form.cleaned_data["login"],
				"password": form.cleaned_data["password"],
			}

			prod = models.Product(login = data["login"], password = data["password"])
			prod.save()
	

		return redirect('/sign_in/')
	else:
		return render(request, 'sign_up/sign_up.html')