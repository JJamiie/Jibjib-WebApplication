"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import include, url, patterns
from django.contrib import admin
from jibjib import views
from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    # api
    # url(r'^api/question/$', views.post_question,name='post_question'),
    # url(r'^api/question/(?P<pk>[0-9]+)$', views.question_detail, name='question_detail'),
    url(r'^api-token-auth/', obtain_auth_token),

    url(r'^api/users/$', views.userList.as_view() ,name='get_user'),

    url(r'^api/questions/$', views.questionList.as_view() ,name='post_question'),
    url(r'^api/questions/(?P<pk>[0-9]+)$', views.questionDetail.as_view() , name='question_detail'),
    url(r'^api/questions/own/$', views.questionOwn.as_view() , name='question_own'),
	url(r'^api/answers/$', views.answerList.as_view() ,name='post_answer'),
    url(r'^api/answers/(?P<pk>[0-9]+)$', views.answerDetail.as_view() , name='answer_detail'),
    url(r'^api/answers/id/(?P<idQuestion>[0-9]+)$', views.answerOfQuestion.as_view() , name='answer_question'),

    url(r'^api/comments/$', views.commentList.as_view() ,name='post_comment'),
    url(r'^api/comments/(?P<pk>[0-9]+)$', views.commentDetail.as_view() , name='comment_detail'),

    url(r'^api/userProfiles/$', views.userProfileList.as_view() ,name='post_userProfile'),
    url(r'^api/userProfiles/(?P<pk>[0-9]+)$', views.userProfileDetail.as_view() , name='userProfile_detail'),
    url(r'^api/userProfiles/own/$', views.userProfileOwn.as_view() , name='userProfile_own'),

    url(r'^api/votes/$', views.voteList.as_view(), name='post_vote'),
    url(r'^api/votes/(?P<pk>[0-9]+)$', views.voteDetail.as_view() , name='vote_detail'),


]

urlpatterns += patterns('',(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))
