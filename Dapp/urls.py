
from django.urls import path
from . import views 

urlpatterns = [
    path('print',views.hello),
    path('print1',views.hello1)
   
]
