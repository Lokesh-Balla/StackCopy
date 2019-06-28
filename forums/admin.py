from django.contrib import admin
from forums.models import *


# Register your models here.
admin.site.register(Questions)
admin.site.register(Answers)
admin.site.register(Tags)
admin.site.register(QueTag)
admin.site.register(VotesQuestion)
admin.site.register(VotesAnswers)