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
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect("questions")

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


class ViewQuestion(View):
    def get(self, request, **kwargs):
        famous_tags = Tags.objects.values('tag_name').annotate(count=Count('questions__pk')).order_by('-count')[:10]
        popular_questions = Questions.objects.values('title').annotate(
            count=Count('pk', filter=Q(votes__vote=1))).order_by('-count')

        return render(
            request,
            template_name='forums/viewquestion.html',
            context={
                'q_id': kwargs['pk'],
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


class PostAnswerApi(APIView):
    def post(self, request, **kwargs):
        data = request.data

        form = Answers()

        form.question = Questions.objects.get(pk=kwargs['pk'])
        form.user = User.objects.get(pk=data['user_id'])
        form.desc = data['desc']
        form.save()
        return Response({'status': 'posted successfully'}, status=status.HTTP_201_CREATED)


class UpdateVotesQuestionsApi(APIView):
    def post(self, request):
        data = request.data

        vote = Votes.objects.filter(questions__id=data["q_id"], user__id=data["user_id"])

        if vote.exists():
            vote = vote[0]
            if vote.vote == data["value"]:
                vote.delete()
            else:
                vote.vote = data["value"]
                vote.save()
        else:
            form = Votes()
            form.user = User.objects.get(pk=data["user_id"])
            form.vote = data["value"]
            form.save()
            que = Questions.objects.get(pk=data["q_id"])
            que.votes.add(form)

        return Response({'status': 'updated successfully'}, status=status.HTTP_201_CREATED)


class UpdateVotesAnswersApi(APIView):
    def post(self, request):
        data = request.data

        vote = Votes.objects.filter(answers__id=data["a_id"], user__id=data["user_id"])

        if vote.exists():
            vote = vote[0]
            if vote.vote == data["value"]:
                vote.delete()
            else:
                vote.vote = data["value"]
                vote.save()
        else:
            form = Votes()
            form.user = User.objects.get(pk=data["user_id"])
            form.vote = data["value"]
            form.save()
            ans = Answers.objects.get(pk=data["a_id"])
            ans.votes.add(form)

        return Response({'status': 'updated successfully'}, status=status.HTTP_201_CREATED)


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
        if "phrase" in kwargs:
            self.queryset = Questions.objects.filter(title__contains=kwargs['phrase']).order_by("-last_updated")
        elif "pk" in kwargs:
            self.queryset = Questions.objects.filter(pk=kwargs['pk'])
        return self.list(request, **kwargs)


class QuestionAnswersApi(mixins.ListModelMixin, generics.GenericAPIView):
    serializer_class = QuestionAnswersSerializer
    queryset = None

    def get(self, request, **kwargs):
        self.queryset = Answers.objects.filter(question__pk=kwargs['pk'])
        return self.list(request, **kwargs)
