# Generated by Django 2.2.1 on 2019-06-03 01:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 3, 1, 47, 41, 651600, tzinfo=utc)),
        ),
    ]
