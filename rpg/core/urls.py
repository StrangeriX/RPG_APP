from urllib import request
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.CharacterList.as_view(), name='characters'),
    path('create/', views.CharacterCreate.as_view(), name='character_create'),
    path('<int:pk>', views.CharacterDetail.as_view(), name='character_detail'),
]
