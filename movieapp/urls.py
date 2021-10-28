from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('result/', views.searchresult, name='result'),
    path('movies/', views.movies, name='movies'),
    path('celebrities/', views.celebrities, name='celebrities'),
    path('top_movies/', views.top_movies, name='top_movies'),
    path('moviedetails/<str:pk>', views.moviedetails, name='moviedetails'),
    path('blog_details/', views.blog_details, name='blog_details'),
    path('blog/', views.blog, name='blog'),
    path('login/', views.login, name='login'),
]    