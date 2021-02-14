from django.shortcuts import render, redirect

from . import forms

from sign_up import models 
# Create your views here.

def sign_in_page(request):
	if request.method == "POST":
		form = forms.SignIn(request.POST)
		print(form.is_valid())

		# if len(models.User.objects.get(login = form.cleaned_data["login"], password = form.cleaned_data["password"])) != 0:
		# 	print(1)
		# else:
		# 	print(0)
		if form.is_valid() == True:
			try:
				models.User.objects.get(login = form.cleaned_data["login"], password = form.cleaned_data["password"])
				print(1)
				return redirect('/')
			except:
				print(0)
				return render(request, 'sign_in/sign_in.html')
		else:
			return render(request, 'sign_in/sign_in.html')
	else:
		return render(request, 'sign_in/sign_in.html')