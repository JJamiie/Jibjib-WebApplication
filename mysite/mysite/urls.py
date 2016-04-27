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


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    # api
    # url(r'^api/question/$', views.post_question,name='post_question'),
    # url(r'^api/question/(?P<pk>[0-9]+)$', views.question_detail, name='question_detail'),

    url(r'^api/questions/$', views.questionList.as_view() ,name='post_question'),
    url(r'^api/questions/(?P<pk>[0-9]+)$', views.questionDetail.as_view() , name='question_detail'),
]
