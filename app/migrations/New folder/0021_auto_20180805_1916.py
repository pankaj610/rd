# Generated by Django 2.0.7 on 2018-08-05 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_vo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vo',
            name='student',
        ),
        migrations.AddField(
            model_name='vo',
            name='vote',
            field=models.IntegerField(default=0),
        ),
    ]
