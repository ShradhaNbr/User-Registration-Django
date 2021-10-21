from django.urls import path

from . import views

urlpatterns = [
    path('register', views.register_request, name='registeruser'),
    path('login', views.login, name='login'),
]
