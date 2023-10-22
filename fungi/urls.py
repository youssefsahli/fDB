from django.urls import path
from . import views

urlpatterns = [
    path('', views.fungi_list, name='fungi_list'),
    path('<int:fungi_id>/', views.fungi_detail, name='fungi_detail'),
    path('quiz/', views.quiz, name='quiz'),
]

