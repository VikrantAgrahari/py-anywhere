# Generated by Django 3.0.5 on 2020-05-01 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genius', '0013_create_class_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='left_amount',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
