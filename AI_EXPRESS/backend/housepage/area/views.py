# 홈페이지 페이지 뷰 관리
# https://velog.io/@yvvyoon/django-rest-framework-2

from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import generics, mixins
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView

from .serializers import DongSerializer
from .serializers import KeywordSerializer
from .models import Dong
from .models import SearchKeyword

from urllib import parse

from numpy import array
from keras.models import Sequential
from keras.layers import Dense, Dropout, BatchNormalization, Activation
from keras.losses import MeanAbsolutePercentageError 
from keras.callbacks import Callback, EarlyStopping
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from keras import optimizers

import matplotlib.pyplot as plt
import numpy as np

import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


# Create your views here.

class DongList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Dong.objects.all()
    serializer_class = DongSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request)
    
    def post(self, request, *args, **kwargs):
         return self.create(request)

class DongDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Dong.objects.all()
    serializer_class = DongSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class KeywordList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = SearchKeyword.objects.all()
    serializer_class = KeywordSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request)
    
    def post(self, request, *args, **kwargs):
         return self.create(request)

class KeywordDetail(generics.ListAPIView):
    serializer_class = KeywordSerializer
    serializer_class = DongSerializer
    
    def get_queryset(self):
        # 동별 시설 input 설정
        # (하도 불러오기 안 돼서 임시로 절대경로 입력, 다른 컴퓨터에서 실행 시 꼭 수정)
        input_std = pd.read_csv("C:/Users/ATRON/source/vscode/django/server/housepage/data/input_std.csv", index_col = None, encoding="CP949")
        input = input_std.values

        # query string을 통해 keyword 입력 받아오기
        keyword_string = parse.unquote(self.request.GET.get('keyword', ''))
        keyword = keyword_string.split(',')
        tmp = SearchKeyword.objects.filter(keyword__in=keyword)

        # query string parameter를 통해 연령대, 모델 weight값 조정 수치 저장
        age_group = int(self.request.GET.get('age', ''))

        # keyword에 지정되어 있는 각 field의 true 갯수 count
        num_true = [1 for i in range(15)]

        alpha = 0.5

        for i in tmp.values():
            idx = 0
            print(i)
            for key, values in i.items():
                if key == 'id' or key == 'keyword':
                    continue
                elif values is True:
                    num_true[idx] += alpha
                idx += 1
        print(num_true)

        # input에 num_true값 조정
        input *= num_true

        # 인공지능 모델 주입
        # (하도 불러오기 안 돼서 임시로 절대경로 입력, 다른 컴퓨터에서 실행 시 꼭 수정)
        if age_group == 20:
            AImodel = keras.models.load_model('C:/Users/ATRON/source/vscode/django/server/housepage/model/20model.h5')
        elif age_group == 30:
            AImodel = keras.models.load_model('C:/Users/ATRON/source/vscode/django/server/housepage/model/30model.h5')
        elif age_group == 40:
            AImodel = keras.models.load_model('C:/Users/ATRON/source/vscode/django/server/housepage/model/40model.h5')
        elif age_group == 50:
            AImodel = keras.models.load_model('C:/Users/ATRON/source/vscode/django/server/housepage/model/50model.h5')
        elif age_group == 60:
            AImodel = keras.models.load_model('C:/Users/ATRON/source/vscode/django/server/housepage/model/60model.h5')
        elif age_group == 70:
            AImodel = keras.models.load_model('C:/Users/ATRON/source/vscode/django/server/housepage/model/70model.h5')
        else:   # age_group == 80 or age_group == 90
            AImodel = keras.models.load_model('C:/Users/ATRON/source/vscode/django/server/housepage/model/80model.h5')

        # 모든 동 row를 AImodel에 대입해 계산, 424개의 동별로 점수가 나옴
        out_score = AImodel.predict(input).reshape(424)

        # 점수 오름차순 정렬 후 해당 값의 index를 배열에 저장
        arr_index = np.argsort(out_score)
        
        # 가장 높은 점수를 받은 index를 result 배열에 저장
        result = [arr_index[-1], arr_index[-2], arr_index[-3], arr_index[-4], arr_index[-5], arr_index[-6]] + np.array([1])

        # 순위 순서 저장
        for post in queryset:
            if post.id == result[0]:
                post.out_rank = '1'
            elif post.id == result[1]:
                post.out_rank = '2'
            elif post.id == result[2]:
                post.out_rank = '3'
            elif post.id == result[3]:
                post.out_rank = '4'
            elif post.id == result[4]:
                post.out_rank = '5'
            elif post.id == result[5]:
                post.out_rank = '6'

        # Dong에서 데이터 추출 및 전송
        queryset = Dong.objects.filter(id__in=result).order_by('out_rank')
        serializer = DongSerializer(queryset, many=True)

        return serializer.data

def display(request):
    params = [
        request.GET.get('park','0'),
        request.GET.get('kindergarten','0'),
        request.GET.get('school_elementary','0'),
        request.GET.get('school_middle','0'),
        request.GET.get('school_high','0'),
        request.GET.get('school_special','0'),
        request.GET.get('hagwon','0'),
        request.GET.get('leisure','0'),
        request.GET.get('restaurant','0'),
        request.GET.get('medical','0'),
        request.GET.get('air_pollution','0'),
        request.GET.get('cctv','0'),
        request.GET.get('senior_center','0'),
        request.GET.get('sport_facility','0'),
        request.GET.get('library','0')]
    return HttpResponse("%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s" % 
        (params[0], params[1], params[2], params[3], params[4], params[5], params[6], params[7], params[8], params[9], params[10], params[11], params[12], params[13], params[14]))

def index(request):
    return HttpResponse("Hello, world. This is head-first page")

def detail(request, question_id):
    return HttpResponse("NO. %s" % question_id)

def test(request):
    return HttpResponse("test page")

def db(request):
    dong = Dong.objects.all()
    context = {'dong':dong}
    return render(request, 'area/index.html', context)