from django.views import View
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from forums.forms import *
from django.db.utils import *


class HomePage(View):
    def get(self, request, **kwargs):
        login_form = LoginForm(prefix="login")
        sign_up_form = SignUpForm(prefix="signup")
        return render(
            request,
            template_name='forums/home.html',
            context={
                'login_form': login_form,
                'sign_up_form': sign_up_form,
            },
        )

    def post(self, request, **kwargs):
        login_form = LoginForm(request.POST, prefix="login")
        sign_up_form = SignUpForm(request.POST, prefix="signup")

        if login_form.is_valid():
            if login_form.is_valid():
                user = authenticate(request, username=login_form.cleaned_data['username'],
                                    password=login_form.cleaned_data['password'])
                if user is not None:
                    login(request, user)
                    return redirect('questions')
                else:
                    return redirect('login')

        if sign_up_form.is_valid():
            try:
                user = User.objects.create_user(**sign_up_form.cleaned_data)
                user.save()
                if user is not None:
                    login(request, user)
                    return redirect('questions')
            except IntegrityError as ie:
                return redirect('signup')


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('questions')