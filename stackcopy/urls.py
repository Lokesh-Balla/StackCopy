"""stackcopy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from forums.views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Forms urls
    path('', HomePage.as_view(), name='home'),
    path('login', HomePage.as_view(), name='login'),
    path('signup', HomePage.as_view(), name='signup'),
    path('logout', Logout.as_view(), name='logout'),

    path('questions', QuestionsView.as_view(), name='questions'),
    path('askquestion', AskQuestionView.as_view(), name='askquestion'),

    # small hack for making redirect in frontend easy
    path('viewquestion/', ViewQuestion.as_view(), name='viewquestion'),
    path('viewquestion/<int:pk>', ViewQuestion.as_view(), name='viewquestion_2'),

    # API Calls
    path('api/questions', QuestionsApi.as_view(), name='questions_api'),
    path('api/questions/<int:pk>', QuestionsApi.as_view(), name='questions_api_pk'),
    path('api/questions/<str:phrase>', QuestionsApi.as_view(), name='questions_api_phrase'),
    path('api/askquestion', AskQuestionApi.as_view(), name='askquestion_api'),
    path('api/quesitonanswer/<int:pk>', QuestionAnswersApi.as_view(), name='questionanswer'),
    path('api/postanswer/<int:pk>', PostAnswerApi.as_view(), name='postanswer'),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
