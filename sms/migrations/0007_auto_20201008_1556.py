# Generated by Django 3.1 on 2020-10-08 14:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0006_auto_20201008_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='time',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='receive',
            name='time',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
