from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('start-quiz/', views.start_quiz, name='start_quiz'),
    path('submit-quiz/', views.submit_quiz, name='submit_quiz'),
]
