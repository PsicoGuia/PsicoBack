# Generated by Django 2.0.4 on 2018-08-26 04:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medic', '0019_auto_20180826_0324'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attentionchannel',
            old_name='titulo',
            new_name='title',
        ),
    ]
