from django.contrib.auth.models import User   #generic User class provided by django
from django import forms  # imports forms

class UserForm(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput) 
	
	class Meta:    # meta class provides information about the class
		model = User
		fields = ['username' , 'email' , 'password']  # list which stores info about what will appear on  the page for user
