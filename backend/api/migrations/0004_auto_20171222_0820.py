# Generated by Django 2.0 on 2017-12-22 12:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20171222_0809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='date_in',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 22, 8, 20, 8, 372310)),
        ),
    ]