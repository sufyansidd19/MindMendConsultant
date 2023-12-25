from django.urls import path
from module1 import views

urlpatterns = [
    path('',views.index,name='index'),
]