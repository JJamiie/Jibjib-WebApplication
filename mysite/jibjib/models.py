from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Question(models.Model):
	owner = models.ForeignKey(User, related_name='question_owner',null=True)
	title = models.CharField(max_length=200)
	description = models.TextField()

	def __unicode__(self): 
		return "Title: " + self.title + ",    Description: " + self.description 

