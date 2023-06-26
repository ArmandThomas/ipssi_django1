from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='index'),
    path('game/<int:game_id>', views.gamePage, name='game'),
    path('login', views.loginPage, name='login'),
    path('register', views.registerPage, name='register'),
    path('user_info', views.profilPage, name='user_info')
]
