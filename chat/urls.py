from django.contrib import admin
from django.urls import path,include
from . import views
#from accounts.views import UserInfo
from django.contrib.auth.models import User
app_name = 'chat'
#uid = UserInfo()
urlpatterns = [
    
#    path('',views.home,name="home"),
    path('<int:uid>/', views.chat, name='chat'),
#    path('<int:uid>/', views.room, name='room'),
#    path('<str:ro>/', views.room, name='room'),
]
