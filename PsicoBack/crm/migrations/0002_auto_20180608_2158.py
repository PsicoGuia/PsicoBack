# Generated by Django 2.0.4 on 2018-06-08 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='notification',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='person',
            name='term',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='term_abausdata',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
