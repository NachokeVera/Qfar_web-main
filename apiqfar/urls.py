from django.urls import path,re_path
from . import views

urlpatterns = [
    path('', views.getData),
    re_path('login',views.login),
    re_path('register',views.register),
    re_path('verify',views.verify),
]