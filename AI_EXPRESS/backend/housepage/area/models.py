# model 정의 코드
# 여기에서 model의 인자를 설정
# 인자 변경 후 migration 필수

from django.db import models

# Create your models here.
# 항목 추가 시 default parameter 꼭 추가할 것
class Dong(models.Model):
    district = models.CharField(default='', max_length=5)
    name = models.CharField(default='', max_length=8)
    population_all = models.IntegerField(default=0)

    park = models.IntegerField(default=0)
    kindergarten = models.IntegerField(default=0)
    school_elementary = models.IntegerField(default=0)
    school_middle = models.IntegerField(default=0)
    school_high = models.IntegerField(default=0)
    school_special = models.IntegerField(default=0)
    hagwon = models.IntegerField(default=0)
    leisure = models.IntegerField(default=0)
    restaurant = models.IntegerField(default=0)
    medical = models.IntegerField(default=0)
    air_pollution = models.FloatField(default=0)
    cctv = models.IntegerField(default=0)
    senior_center = models.IntegerField(default=0)
    sport_facility = models.IntegerField(default=0)
    library = models.IntegerField(default=0)

    out_rank = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class SearchKeyword(models.Model):
    keyword = models.CharField(default='', max_length=255)

    park = models.BooleanField(default=False)
    kindergarten = models.BooleanField(default=False)
    school_elementary = models.BooleanField(default=False)
    school_middle = models.BooleanField(default=False)
    school_high = models.BooleanField(default=False)
    school_special = models.BooleanField(default=False)
    hagwon = models.BooleanField(default=False)
    leisure = models.BooleanField(default=False)
    restaurant = models.BooleanField(default=False)
    medical = models.BooleanField(default=False)
    air_pollution = models.BooleanField(default=False)
    cctv = models.BooleanField(default=False)
    senior_center = models.BooleanField(default=False)
    sport_facility = models.BooleanField(default=False)
    library = models.BooleanField(default=False)

    def __str__(self):
        return self.keyword