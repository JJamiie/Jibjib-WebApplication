from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
from datetime import datetime
# Create your models here.

# This code is triggered whenever a new user has been created and saved to the database
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class UserProfile(models.Model):
	owner = models.ForeignKey(User, related_name='userprofile_owner')
	firstname = models.CharField(max_length=200)
	lastname = models.CharField(max_length=200)
	email = models.EmailField(blank=True)
	user_pic = models.ImageField(upload_to = 'pic_folder', default = 'pic_folder/default_profile.png')
	work = models.CharField(max_length=200)

	def __unicode__(self):
		return "Name: " + self.firstname + ",   work: " + self.work

class Comment(models.Model):
	owner = models.ForeignKey(User, related_name='comment_owner')
	commenter = models.ForeignKey(User,related_name='commenter_user')
	content = models.TextField()

	def __unicode__(self):
		return "Owner: "+ self.owner.username + ",   Commenter: " + self.commenter.username


class Question(models.Model):
    LANG = (
        ('Thai', 'Thai'),
        ('English', 'English'),
        ('Chinese', 'Chinese'),
    )
    owner = models.ForeignKey(User, related_name='question_owner')
    title = models.CharField(max_length=100)
    content = models.TextField()
    from_lang = models.CharField(max_length=20,choices=LANG)
    to_lang = models.CharField(max_length=20,choices=LANG)
    created_at = models.DateTimeField(default=datetime.now)
    def __unicode__(self):
        return "Owner: "+ self.owner.username +",   Title: " + self.title + ",    Description: " + self.content +",   FROM "+ self.from_lang+ " to " + self.to_lang

class Answer(models.Model):
	owner = models.ForeignKey(User, related_name='answer_owner')
	question  = models.ForeignKey(Question, related_name='answer_question')
	content = models.TextField()

	def __unicode__(self):
		return "Owner: " + self.owner.username + ",   content: " + self.content

class Vote(models.Model):
    owner = models.ForeignKey(User, related_name='vote_owner')
    answer = models.ForeignKey(Answer, related_name='vote_answer')
    score = models.SmallIntegerField(default=0)

    def __unicode__(self):
        return "Owner: " + self.owner.username + ", answer: " + self.answer.question.title +", vote: " + str(self.score)
