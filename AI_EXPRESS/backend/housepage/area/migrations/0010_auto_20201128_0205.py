# Generated by Django 3.1.3 on 2020-11-27 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('area', '0009_auto_20201128_0049'),
    ]

    operations = [
        migrations.AddField(
            model_name='dong',
            name='out_rank',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='dong',
            name='out_score',
            field=models.FloatField(default=0),
        ),
    ]
