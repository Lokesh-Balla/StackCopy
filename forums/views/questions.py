from django.views import View
from django.shortcuts import redirect, render
from rest_framework import generics, mixins
from django.contrib.auth.models import User
from forums.models import *
from django.db.models import Count, Q
from rest_framework.views import APIView
from forums.serializers import *
from rest_framework.response import Response
from rest_framework import status
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


class AskQuestionView(View):
    def get(self, request, **kwargs):
        famous_tags = Tags.objects.values('tag_name').annotate(count=Count('questions__pk')).order_by('-count')[:10]
        popular_questions = Questions.objects.values('title').annotate(
            count=Count('pk', filter=Q(votes__vote=1))).order_by('-count')

        return render(
            request,
            template_name='forums/askquestions.html',
            context={
                'famous_tags': famous_tags,
                'popular_questions': popular_questions,
            },
        )


class AskQuestionApi(APIView):
    def post(self, request):
        data = request.data

        form = Questions()

        form.user = User.objects.get(pk=data['user_id'])
        form.title = data['title']
        form.desc = data['desc']
        form.save()

        for x in data["tags"].split():
            if Tags.objects.filter(tag_name=x).exists():
                tag = Tags.objects.get(tag_name=x)
                form.tags.add(tag)
            else:
                tag = Tags(tag_name=x)
                tag.save()
                form.tags.add(tag)

        return Response({'status': 'posted successfully'}, status=status.HTTP_201_CREATED)


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
