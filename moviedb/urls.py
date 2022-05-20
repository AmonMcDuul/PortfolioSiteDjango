from django.urls import path
from . import views

urlpatterns = [
    path('', views.movieDb, name='moviedb'),
    path('movie/<str:pk>/', views.selectedMovie, name='selectedmovie'),
    path('savedmovies/', views.savedMovies, name='savedmovies'),
]