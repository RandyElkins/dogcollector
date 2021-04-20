from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home_page'),
  path('about/', views.about, name='about_page'),
  path('dogs/', views.dogs_index, name='dogs_index_page'),
  path('dogs/<int:dog_id>/', views.dogs_detail, name='detail'),
  path('dogs/create/', views.DogCreate.as_view(), name='dogs_create'),
  path('dogs/<int:pk>/update/', views.DogUpdate.as_view(), name='dogs_update'),
  path('dogs/<int:pk>/delete/', views.DogDelete.as_view(), name='dogs_delete'),
]