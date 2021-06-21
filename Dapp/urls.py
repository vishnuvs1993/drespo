
from os import name
from django.urls import path
from . import views 

urlpatterns = [
    path('print',views.hello),
    path('vishnu',views.hello1, name='vishnu')
   
]
