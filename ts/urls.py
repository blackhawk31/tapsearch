from django.urls import path
from .views import *


urlpatterns = [
    path('',        home,       name ='home'),
    path('clear',   clear,      name = 'clear'),
    path('success', success,    name ='success'),
    path('result',  query,      name ='result'),
    path('index',   index,      name ='index'),
    path('search',  search,     name ='search'),
    path('t/',   HomeAPIView.as_view(),  name='home-view'),
]
