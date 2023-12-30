from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sessions', views.sessions, name='sessions'),
    path('auth', views.auth, name='auth'),
    path('logged_in', views.login_view, name='login_view'),
]
