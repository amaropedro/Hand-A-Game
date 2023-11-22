from django.urls import path
from . import views

urlpatterns = [
  path('allgames', views.listTest, name="list"),
  path('login', views.login_view, name="login"),
  path('sign_up', views.signup_view, name="signup"),
  path('home', views.home, name="home")
]