# Generated by Django 2.0.4 on 2018-08-26 02:48

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medic', '0016_auto_20180821_0147'),
    ]

    operations = [
        migrations.DeleteModel('Office'),
        migrations.DeleteModel('Chat'),
        migrations.DeleteModel('HomeVisit'),
    ]