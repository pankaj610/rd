# Generated by Django 2.0.7 on 2018-08-05 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_delete_vote'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Student')),
            ],
        ),
    ]
