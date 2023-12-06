from django.urls import path
from . import views

urlpatterns = [
  path('sign_up', views.signup_view, name="signup"),
  path('login', views.login_view, name="login"),
  path('logout', views.logout_view, name="logout"),
  path('', views.login_view, name="login"),
  path('home', views.home_view, name="home"),
  path('my_games', views.myGames_view, name="myGames"),
  path('add_game', views.addGame_view, name="addGame")
]