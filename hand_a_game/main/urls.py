from django.urls import path
from . import views

urlpatterns = [
  path('all_games', views.allGames_view, name="allGames"),
  path('login', views.login_view, name="login"),
  path('sign_up', views.signup_view, name="signup"),
  path('home', views.home_view, name="home"),
]