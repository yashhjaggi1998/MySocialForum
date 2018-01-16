# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.views import generic
from django.views.generic import View
from .forms import UserForm
from django.template import loader
from .models import User,Chat
from django.http import HttpResponse , HttpResponseRedirect
# Create your views here.

def index(request):
	all_users = User.objects.all()
	template = loader.get_template('message/index.html')
	context = {
		'all_users' : all_users,
		}
	return HttpResponse(template.render(context,request))
	
	
def detail(request , user_id):
	user = User.objects.get( pk = user_id )
	template = loader.get_template('message/detail.html')
	context={
		'user' : user,
	}
	return HttpResponse(template.render(context,request))
	
	
def home(request):
	template = loader.get_template('message/home.html')
	context={}
	return HttpResponse(template.render(context,request))
	
	
class UserFormView(View):
	form_class = UserForm
	template_name = 'message/signup.html'
	
	def get(self,request):
		form = self.form_class(None)
		return render(request,self.template_name,{'form' : form})
	
	def post(self,request):
		user = self.form_class(request.POST)
	
		if form.is_valid():
		
			username = form.cleaned_data('username')
			password = form.cleaned_data('password')
			user.set_password(password)
			user.save()
