# Generated by Django 3.0.3 on 2020-04-30 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('genius', '0014_students_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='image',
        ),
    ]
