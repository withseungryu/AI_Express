# 홈페이지 링크 관리

from django.urls import path

from . import views
from area.views import DongList
from area.views import DongDetail
from area.views import KeywordList
from area.views import KeywordDetail

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('test/', views.test, name='test'),
    path('db/', views.db, name='db'),
    path('display/', views.display, name='display'),
    
    path('api/dong/', DongList.as_view()),
    path('api/dong/<int:pk>/', DongDetail.as_view()),
    path('api/keyword/', KeywordDetail.as_view()),
    path('api/keyword/all', KeywordList.as_view()),
]