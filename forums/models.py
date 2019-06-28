from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Questions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False, blank=False)
    desc = models.TextField(null=False, blank=False)
    last_updated = models.DateTimeField(auto_now=True)
    date_closed = models.DateTimeField(null=True, blank=True)


class Answers(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    desc = models.TextField(null=False, blank=False)
    answered_date = models.DateTimeField(auto_now=True)


class Tags(models.Model):
    tag_name = models.CharField(max_length=50, null=False, blank=False)


# Yeah I know not the best name
class QueTag(models.Model):
    qid = models.ForeignKey(Questions, on_delete=models.CASCADE)
    tid = models.ForeignKey(Tags, on_delete=models.CASCADE)


class VotesQuestion(models.Model):
    qid = models.ForeignKey(Questions, on_delete=models.CASCADE)
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    up_vote = models.BooleanField(default=False)
    down_vote = models.BooleanField(default=False)


class VotesAnswers(models.Model):
    qid = models.ForeignKey(Questions, on_delete=models.CASCADE)
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    up_vote = models.BooleanField(default=False)
    down_vote = models.BooleanField(default=False)
