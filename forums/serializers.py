from rest_framework import serializers
from forums.models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ("password", "last_login", "is_superuser", "groups", "user_permissions", "is_staff")


class QuestionsSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Questions
        fields = ("id", "title", "desc", "last_updated", "date_closed", "tags", "votes", "user")
        depth = 1
