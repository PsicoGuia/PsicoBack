# Generated by Django 2.0.4 on 2018-08-26 03:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medic', '0018_auto_20180826_0250'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageattentionchannel',
            name='attention_channel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='medic.AttentionChannel'),
        ),
        migrations.AddField(
            model_name='scheduleattentionchannel',
            name='attention_channel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='medic.AttentionChannel'),
        ),
    ]
