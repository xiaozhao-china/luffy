from django.urls import path, re_path
from django.shortcuts import HttpResponse
from . import views

urlpatterns = [
    path('',views.Home.as_view()),
    path('banner/',views.BannerListAPIView.as_view()),
]



