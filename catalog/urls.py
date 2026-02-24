from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),           # главная страница
    path('contacts/', views.contacts, name='contacts'),  # контакты
]