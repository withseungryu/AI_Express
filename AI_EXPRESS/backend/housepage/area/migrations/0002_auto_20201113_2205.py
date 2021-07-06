# Generated by Django 3.1.2 on 2020-11-13 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('area', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dong',
            name='district',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AlterField(
            model_name='dong',
            name='name',
            field=models.CharField(default='', max_length=8),
        ),
        migrations.AlterField(
            model_name='dong',
            name='park',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dong',
            name='school',
            field=models.FloatField(default=0),
        ),
    ]