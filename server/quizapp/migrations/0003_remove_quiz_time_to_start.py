# Generated by Django 3.0.4 on 2020-03-12 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0002_quiz_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='time_to_start',
        ),
    ]
