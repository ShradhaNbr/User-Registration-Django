from django.urls import path

from . import views
from .views import NoteList

urlpatterns = [
    path('', NoteList.as_view()),


]

