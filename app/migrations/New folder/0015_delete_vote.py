# Generated by Django 2.0.7 on 2018-08-05 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_remove_vote_student'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Vote',
        ),
    ]
