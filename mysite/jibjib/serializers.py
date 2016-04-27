from jibjib.models import *
from rest_framework import serializers

class QuestionSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')

	class Meta:
		model = Question
		fields = ('title', 'description','owner')
