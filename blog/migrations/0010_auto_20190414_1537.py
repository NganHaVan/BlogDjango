# Generated by Django 2.1.7 on 2019-04-14 15:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20190414_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 14, 15, 37, 28, 486300, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 14, 15, 37, 28, 485337, tzinfo=utc)),
        ),
    ]
