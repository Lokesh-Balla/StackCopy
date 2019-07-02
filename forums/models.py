from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Questions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False, blank=False)
    desc = models.TextField(null=False, blank=False)
    last_updated = models.DateTimeField(auto_now=True)
    date_closed = models.DateTimeField(null=True, blank=True)
    tags = models.ManyToManyField('Tags', blank=True)
    votes = models.ManyToManyField('Votes', blank=True)

    def __str__(self):
        return self.title


class Answers(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    desc = models.TextField(null=False, blank=False)
    answered_date = models.DateTimeField(auto_now=True)
    votes = models.ManyToManyField('Votes', blank=True)


class Tags(models.Model):
    tag_name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.tag_name


class Votes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vote = models.IntegerField(default=0)
