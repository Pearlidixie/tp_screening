# Generated by Django 2.0.4 on 2018-04-19 10:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tp_screening', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjectscreening',
            name='report_datetime',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 19, 10, 9, 57, 245995), help_text='Date and time of report.', verbose_name='Report Date and Time'),
        ),
    ]
