from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home_page'),
  path('about/', views.about, name='about_page'),
  path('dogs/', views.dogs_index, name='dogs_index_page'),
#   path('dogs/<int:dog_id>/', views.dogs_detail, name='detail'),
]