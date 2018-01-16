# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class User(models.Model): 
	name = models.CharField(max_length = 150 , null = True)
	status = models.CharField(max_length = 50 , null = True)
	
	def __str__(self):
		return self.name
		
class Chat(models.Model):
	user = models.ForeignKey(User , on_delete = models.CASCADE)
	source_user = models.CharField(max_length = 100, null = True)
	destination_user = models.CharField(max_length = 100 , null = True)
	message = models.CharField(max_length = 200 , null = True)
	#time = models.DateTimeField('Send/recieve Time')
	
	def __str__(self):
		return self.source_user + "-" + self.destination_user
