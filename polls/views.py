# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render , get_object_or_404
from .models import Question,Choice
from django.template import loader
from django.urls import reverse
from django.views import generic
 
'''def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	template = loader.get_template('polls/index.html')
	context = {
		'latest_question_list' : latest_question_list,
		}
	#text = 'Hello World. U are at the polls index'
	return HttpResponse(template.render(context,request))
	
#/polls/45  => opens question with primary key = 45 
def detail(request , question_id):
	question = Question.objects.get( pk = question_id )
	context = {
		'question' : question , 
		}
	return render(request,'polls/detail.html' , context)
	
#/polls/45/results  => displays resullts	
def results(request , question_id):
	question = get_object_or_404(Question, pk = question_id)
	context = {
		'question' : question ,
	}
	return render(request , 'polls/result.html' , context)'''
	
#generic view

class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'
	
	def get_queryset(self):
		return Question.objects.order_by('-pub_date')[:5]
	
class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'
		
class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/result.html'
	
#/polls/45/vote  => opens a webpage for users to vote	
def vote(request, question_id):
	question = get_object_or_404(Question , pk = question_id)
	try:
		selected_choice = question.choice_set.get(pk = request.POST['choice'])
	except(KeyError , Choice.DoesNotExist):
		context = {
			'question' : question ,
			'error_message' : "You didn't select a choice.",
		}
		return render(request , 'polls/detail.html' , context)
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return render(request , 'polls/result.html' , { 'question' : question , } )
