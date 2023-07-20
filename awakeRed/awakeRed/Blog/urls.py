from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('tweet/', views.createTweet, name='crear-tweet')
]