from app2.views import *
from django.urls import path

app_name = 'second'

urlpatterns = [
    path('second/',second,name='second'),
    path('second2/',second2,name='second2'),
]