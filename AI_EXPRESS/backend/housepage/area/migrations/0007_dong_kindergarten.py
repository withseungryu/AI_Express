# Generated by Django 3.1.3 on 2020-11-26 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('area', '0006_dong_school_special'),
    ]

    operations = [
        migrations.AddField(
            model_name='dong',
            name='kindergarten',
            field=models.FloatField(default=0),
        ),
    ]