from jibjib.models import *
from rest_framework import serializers

class QuestionSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')

	class Meta:
		model = Question
		fields = ('owner','title', 'content','from_lang','to_lang','id')


class AnswerSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')

	class Meta:
		model = Answer
		fields = ('owner', 'question','content','vote','id')


class CommentSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')

	class Meta:
		model = Comment
		fields = ('owner', 'commenter','content','id')


class UserProfileSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')

	class Meta:
		model = UserProfile
		fields = ('owner', 'firstname','lastname','email','user_pic','work','id')

