from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from jibjib.serializers import *
from jibjib.models import *
from jibjib.permission import IsOwnerOrReadOnly

################################# Model user #################################

class UserMixin(object):
	queryset = User.objects.all().order_by('-id')
	serializer_class = UserSerializer
	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

class userList(UserMixin,generics.ListCreateAPIView):
	pass
################################# Model question #################################

class QuestionMixin(object):
	queryset = Question.objects.all().order_by('-created_at')
	serializer_class = QuestionSerializer
	permission_classes = (IsOwnerOrReadOnly,)

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

class questionList(QuestionMixin,generics.ListCreateAPIView):
	pass

class questionDetail(QuestionMixin,generics.RetrieveUpdateDestroyAPIView):
	pass

class questionOwn(generics.ListCreateAPIView):
	serializer_class = QuestionSerializer
	permission_classes = (IsOwnerOrReadOnly,)
	def get_queryset(self):
		owner = self.request.user
		return Question.objects.filter(owner=owner).order_by('-created_at')

################################# Model answer #################################

class AnswerMixin(object):
	queryset = Answer.objects.all()
	serializer_class = AnswerSerializer
	permission_classes = (IsOwnerOrReadOnly,)

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

class answerList(AnswerMixin,generics.ListCreateAPIView):
	pass

class answerDetail(AnswerMixin,generics.RetrieveUpdateDestroyAPIView):
	pass

class answerOfQuestion(generics.ListCreateAPIView):
	serializer_class = AnswerSerializer
	def get_queryset(self):
		idQuestion = self.kwargs['idQuestion']
		question = Question.objects.filter(id=idQuestion)
		return Answer.objects.filter(question=question)


################################# Model comment #################################

class CommentMixin(object):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer
	permission_classes = (IsOwnerOrReadOnly,)

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

class commentList(CommentMixin,generics.ListCreateAPIView):
	pass

class commentDetail(CommentMixin,generics.RetrieveUpdateDestroyAPIView):
	pass

################################# Model vote #################################

class VoteMixin(object):
	queryset = Vote.objects.all()
	serializer_class = VoteSerializer
	permission_classes = (IsOwnerOrReadOnly,)

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

class voteList(VoteMixin,generics.ListCreateAPIView):
	pass

class voteDetail(VoteMixin,generics.RetrieveUpdateDestroyAPIView):
	pass

################################# UserProfile question #################################

class UserProfileMixin(object):
	queryset = UserProfile.objects.all()
	serializer_class = UserProfileSerializer
	permission_classes = (IsOwnerOrReadOnly,)

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

class userProfileList(UserProfileMixin,generics.ListCreateAPIView):
	pass

class userProfileDetail(UserProfileMixin,generics.RetrieveUpdateDestroyAPIView):
	pass

class userProfileOwn(generics.ListCreateAPIView):
	serializer_class = UserProfileOwnSerializer
	permission_classes = (IsOwnerOrReadOnly,)
	def get_queryset(self):
		owner = self.request.user
		return UserProfile.objects.filter(owner=owner)

#########################################################################################

# Create your views here.
@api_view(['GET', 'POST'])
def post_question(request):

    # List all questions or create a new question.
    if request.method == 'GET':
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def question_detail(request, pk):

    # Get, udpate, or delete a specific task
    try:
        question = Question.objects.get(pk=pk)
    except Question.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = QuestionSerializer(task)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = QuestionSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
