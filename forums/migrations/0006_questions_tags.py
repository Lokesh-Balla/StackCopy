# Generated by Django 2.2.2 on 2019-06-30 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0005_answers_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='tags',
            field=models.ManyToManyField(to='forums.Tags'),
        ),
    ]
