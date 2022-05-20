from django.urls import path
from . import views

urlpatterns = [
    path('', views.apod, name='apod'),
    path('spacenews/', views.spaceNews, name='spacenews'),
    path('marspost/', views.marsPost, name='marspost'),
    path('singlepage/<str:pk>/', views.singlePage, name='singlepage'),
]