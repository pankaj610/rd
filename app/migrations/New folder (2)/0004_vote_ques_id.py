# Generated by Django 2.0.7 on 2018-08-05 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_vote_question_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='ques_id',
            field=models.IntegerField(default=0),
        ),
    ]
