from django.views import View
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from forums.models import *
from django.db.models import Count, Q
from forums.forms import *
from django.db.utils import *


class QuestionsView(View):
    def get(self, request, **kwargs):
        famous_questions = Questions.objects.values('title', 'desc', 'user__username').order_by(
            '-last_updated').annotate(cup=Count('votesquestion', filter=Q(votesquestion__up_vote=True)),
                                      cdwn=Count('votesquestion', filter=Q(votesquestion__down_vote=True)))[:10]
        return render(
            request,
            template_name='forums/questions.html',
            context={
                'fq': famous_questions,
            },
        )

    def post(self, request, **kwargs):
        pass
