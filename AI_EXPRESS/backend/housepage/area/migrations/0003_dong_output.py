# Generated by Django 3.1.3 on 2020-11-26 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('area', '0002_auto_20201113_2205'),
    ]

    operations = [
        migrations.AddField(
            model_name='dong',
            name='output',
            field=models.FloatField(default=0),
        ),
    ]
