# Generated by Django 3.1.3 on 2020-11-27 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('area', '0010_auto_20201128_0205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dong',
            name='out_score',
        ),
    ]
