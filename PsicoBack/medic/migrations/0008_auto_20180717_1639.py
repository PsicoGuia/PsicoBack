# Generated by Django 2.0.4 on 2018-07-17 16:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('medic', '0007_auto_20180717_1631'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scheduleattentionchannel',
            name='duration',
        ),
        migrations.AddField(
            model_name='scheduleattentionchannel',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 17, 16, 39, 29, 325439, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scheduleattentionchannel',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 17, 16, 39, 34, 269037, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
