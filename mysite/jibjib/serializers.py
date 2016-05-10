from jibjib.models import *
from django.contrib.auth.models import User
from rest_framework import serializers
from django.utils import timezone
class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User

class UserProfileSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	class Meta:
		model = UserProfile
		fields = ('owner', 'firstname','lastname','email','user_pic','work','id')

class CommentSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	commenter = serializers.ReadOnlyField(source='commenter.username')
	userprofile = serializers.SerializerMethodField('get_userProfile')

	def get_userProfile(self, obj):
		user = obj.commenter
		userprofile = UserProfile.objects.get(owner=user)
		serializer = UserProfileSerializer(userprofile)
		return serializer.data

	class Meta:
		model = Comment
		fields = ('owner', 'commenter','content','id','userprofile')

class UserProfileOwnSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	count_own_ans = serializers.SerializerMethodField('get_sizeOfAnswer')
	count_own_vote = serializers.SerializerMethodField('get_sizeOfVote')
	own_comment = serializers.SerializerMethodField('get_Comment')

	def get_sizeOfAnswer(self,obj):
		user = self.context['request'].user
		return Answer.objects.filter(owner=user).count()

	def get_sizeOfVote(self,obj):
		user = self.context['request'].user
		answers = Answer.objects.filter(owner=user)
		sum = 0
		for answer in answers:
			sum += Vote.objects.filter(answer=answer).count()
		return sum

	def get_Comment(self,obj):
		user = self.context['request'].user
		comments = Comment.objects.filter(owner=user)
		serializer = CommentSerializer(instance=comments, many=True)
		return serializer.data

	class Meta:
		model = UserProfile
		fields = ('owner', 'firstname','lastname','email','user_pic','work','id','count_own_ans','count_own_vote','own_comment')

class QuestionSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	count_ans = serializers.SerializerMethodField('get_sizeOfAnswer')
	count_vote = serializers.SerializerMethodField('get_sizeOfVote')
	created_at = serializers.SerializerMethodField('change_format_date')

	def get_sizeOfAnswer(self, obj):
		return Answer.objects.filter(question=obj).count()

	def get_sizeOfVote(self, obj):
		answers = Answer.objects.filter(question=obj)
		sum = 0
		for answer in answers:
			count = Vote.objects.filter(answer=answer).count()
			sum += count
		return sum

	def change_format_date(self, obj):
		tz = timezone.get_default_timezone()
		value = timezone.localtime(obj.created_at, timezone=tz)
		return value.strftime('%Y-%m-%d %H:%M')
	class Meta:
		model = Question
		fields = ('owner','title', 'content','from_lang','to_lang','id','count_ans','count_vote','created_at')


class AnswerSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	userprofile = serializers.SerializerMethodField('get_userProfile')
	vote = serializers.SerializerMethodField('count_vote')

	def get_userProfile(self, obj):
		userprofile = UserProfile.objects.get(owner=obj.owner)
		serializer = UserProfileSerializer(userprofile)
		return serializer.data

	def count_vote(self, obj):
		votes = Vote.objects.filter(answer=obj)
		serializer = VoteSerializer(instance=votes, many=True)
		return serializer.data

	class Meta:
		model = Answer
		fields = ('owner', 'question','content','id','userprofile','vote')


class VoteSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	class Meta:
		model = Vote
		fields = ('owner', 'answer','score')
