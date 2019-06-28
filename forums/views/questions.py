from django.views import View
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from forums.forms import *
from django.db.utils import *


class QuestionsView(View):
    def get(self, request, **kwargs):
        return render(
            request,
            template_name='forums/base.html',
        )

    def post(self, request, **kwargs):
        pass
