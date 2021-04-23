from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home_page'),
  path('about/', views.about, name='about_page'),

  # Dog Paths/Routes
  path('dogs/', views.dogs_index, name='dogs_index_page'),
  path('dogs/<int:dog_id>/', views.dogs_detail, name='detail'),
  path('dogs/create/', views.DogCreate.as_view(), name='dog_create'),
  path('dogs/<int:pk>/update/', views.DogUpdate.as_view(), name='dogs_update'),
  path('dogs/<int:pk>/delete/', views.DogDelete.as_view(), name='dogs_delete'),
  path('dogs/<int:dog_id>/add_feeding/', views.add_feeding, name='add_feeding'),
  path('dogs/<int:dog_id>/add_photo/', views.add_photo, name='add_photo'),
  # associate a toy with a dog (M:M)
  path('dogs/<int:dog_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),

  # Toy Paths/Routes
  path('toys/', views.toys_index, name='toys_index_page'),
  path('toys/<int:toy_id>/', views.toys_detail, name='toy_detail'),
  path('toys/create/', views.ToyCreate.as_view(), name='toy_create'),
  path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toy_update'),
  path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toy_delete'),
]