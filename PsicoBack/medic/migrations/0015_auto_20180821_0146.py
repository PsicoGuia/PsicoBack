# Generated by Django 2.0.4 on 2018-08-21 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medic', '0014_patology_extra_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='titulo',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homevisit',
            name='titulo',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='office',
            name='titulo',
            field=models.TextField(blank=True, null=True),
        ),
    ]