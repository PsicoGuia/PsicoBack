# Generated by Django 2.0.4 on 2018-08-21 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medic', '0015_auto_20180821_0146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='titulo',
            field=models.TextField(default='New channel'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='homevisit',
            name='titulo',
            field=models.TextField(default='New Channel'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='office',
            name='titulo',
            field=models.TextField(default='New Channel'),
            preserve_default=False,
        ),
    ]