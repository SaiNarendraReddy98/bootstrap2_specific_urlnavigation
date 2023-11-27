from app1.views import *
from django.urls import path

app_name = 'first'

urlpatterns = [
    path('first/',first,name='first'),
    path('first2/',first2,name='first2'),
    
]