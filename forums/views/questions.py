from django.views import View
from django.shortcuts import redirect, render
from rest_framework import generics, mixins
from django.core.paginator import Paginator
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
        famous_tags = Tags.objects.values('tag_name').annotate(count=Count('questions__pk')).order_by('-count')[:10]
        popular_questions = Questions.objects.values('title').annotate(
            count=Count('pk', filter=Q(votes__vote=1))).order_by('-count')

        return render(
            request,
            template_name='forums/questions.html',
            context={
                'famous_tags': famous_tags,
                'popular_questions': popular_questions,
            },
        )

    def post(self, request, **kwargs):
        pass


# class QuestionsApi(APIView):
#     def get(self, request, **kwargs):
#         if kwargs:
#             queryset = Questions.objects.filter(title__contains=kwargs['phrase'])
#         else:
#             queryset = Questions.objects.all()
#
#         paginator = Paginator(queryset, 1)
#         page = request.GET.get('page')
#         queryset = paginator.get_page(page)
#
#         serializer = QuestionsSerializer(queryset, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)


class QuestionsApi(mixins.ListModelMixin, generics.GenericAPIView):
    serializer_class = QuestionsSerializer
    queryset = Questions.objects.all().order_by("-last_updated")

    def get(self, request, **kwargs):
        if kwargs:
            self.queryset = Questions.objects.filter(title__contains=kwargs['phrase']).order_by("-last_updated")
        return self.list(request, **kwargs)
