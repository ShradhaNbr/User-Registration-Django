from django.urls import path

from . import views
from .views import RegisterView, RegisterLogin

urlpatterns = [
    # path('register', views.register, name='register'),
    # path('login', views.login_user, name='login'),
    path('register/', RegisterView.as_view()),
    path('login/', RegisterLogin.as_view())
    #   path('register/', views.RegisterView, name='register'),
]
