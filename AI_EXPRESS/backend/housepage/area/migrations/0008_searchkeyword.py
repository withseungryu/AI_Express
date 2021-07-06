# Generated by Django 3.1.3 on 2020-11-27 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('area', '0007_dong_kindergarten'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchKeyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(default='', max_length=255)),
                ('park', models.BooleanField(default=False)),
                ('kindergarten', models.BooleanField(default=False)),
                ('school_elementary', models.BooleanField(default=False)),
                ('school_middle', models.BooleanField(default=False)),
                ('school_high', models.BooleanField(default=False)),
                ('school_special', models.BooleanField(default=False)),
                ('hagwon', models.BooleanField(default=False)),
                ('leisure', models.BooleanField(default=False)),
                ('restaurant', models.BooleanField(default=False)),
                ('medical', models.BooleanField(default=False)),
                ('air_pollution', models.BooleanField(default=False)),
                ('cctv', models.BooleanField(default=False)),
                ('senior_center', models.BooleanField(default=False)),
                ('sport_facility', models.BooleanField(default=False)),
                ('library', models.BooleanField(default=False)),
            ],
        ),
    ]
