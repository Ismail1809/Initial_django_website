from django import forms

class SignUp(forms.Form):
	login = forms.CharField(label = "Логин", max_length = 30)
	password = forms.CharField(label = "Пароль", max_length = 30)