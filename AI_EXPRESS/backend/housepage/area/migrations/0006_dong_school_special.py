# Generated by Django 3.1.3 on 2020-11-26 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('area', '0005_auto_20201127_0128'),
    ]

    operations = [
        migrations.AddField(
            model_name='dong',
            name='school_special',
            field=models.FloatField(default=0),
        ),
    ]
