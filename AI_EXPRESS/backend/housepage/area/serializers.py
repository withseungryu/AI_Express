from rest_framework import serializers
from .models import Dong
from .models import SearchKeyword

class DongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dong
        fields = (
            'district',
            'name',
            'population_all',

            'park',
            'kindergarten',
            'school_elementary',
            'school_middle',
            'school_high',
            'school_special',
            'hagwon',
            'leisure',
            'restaurant',
            'medical',
            'air_pollution',
            'cctv',
            'senior_center',
            'sport_facility',
            'library',
            
            'out_rank')

class KeywordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SearchKeyword
        fields = (
            'keyword',

            'park',
            'kindergarten',
            'school_elementary',
            'school_middle',
            'school_high',
            'school_special',
            'hagwon',
            'leisure',
            'restaurant',
            'medical',
            'air_pollution',
            'cctv',
            'senior_center',
            'sport_facility',
            'library')