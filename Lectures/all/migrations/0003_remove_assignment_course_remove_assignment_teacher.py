# Generated by Django 5.0.6 on 2024-05-23 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('all', '0002_assignment_course_assignment_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignment',
            name='course',
        ),
        migrations.RemoveField(
            model_name='assignment',
            name='teacher',
        ),
    ]
