# Generated by Django 2.0.7 on 2018-08-05 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20180805_1857'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vote',
            old_name='questio',
            new_name='question',
        ),
    ]
