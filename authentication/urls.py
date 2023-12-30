from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('authentication/', views.authentication, name="authentication"),
    path('authentication/signup', views.signup, name="signup"),
    path('authentication/signin', views.signin, name="signin"),
    path('authentication/signout', views.signout, name="signout"),

]
