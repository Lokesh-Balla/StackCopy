from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.CharField(max_length=150, blank=True, null=True)


class Questions(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    desc = models.TextField(null=False, blank=False)
    last_updated = models.DateTimeField(auto_now=True)
    date_closed = models.DateTimeField(null=True, blank=True)
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)


class Answers(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    desc = models.TextField(null=False, blank=False)
    answered_date = models.DateTimeField(auto_now=True)
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)


class Tags(models.Model):
    tag_name = models.CharField(max_length=50, null=False, blank=False)


# Yeah I know not the best name
class QueTag(models.Model):
    qid = models.ForeignKey(Questions, on_delete=models.CASCADE)
    tid = models.ForeignKey(Tags, on_delete=models.CASCADE)
