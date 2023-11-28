from django.urls import path
from . import views

urlpatterns = [
  path('sign_up', views.signup_view, name="signup"),
  path('login', views.login_view, name="login"),
  path('home', views.home_view, name="home"),
  path('my_games', views.myGames_view, name="myGames")
]