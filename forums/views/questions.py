from django.views import View
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from forums.models import *
from django.db.models import Count, Q, When
from rest_framework.views import APIView
from forums.serializers import *
from rest_framework.response import Response
from rest_framework import status
import requests
from forums.forms import *
from django.db.utils import *


class QuestionsView(View):
    def get(self, request):
        return render(
            request,
            template_name='forums/questions.html',
        )

    def post(self, request, **kwargs):
        pass


class QuestionsApi(APIView):
    def get(self, request, **kwargs):
        if(kwargs):
            queryset = Questions.objects.filter(title__contains=kwargs['phrase'])
        else:
            queryset = Questions.objects.all()
        serializer = QuestionsSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
