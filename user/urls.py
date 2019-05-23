from django.urls import path
from . import views

urlpatterns = [
    path('login', views.loginView, name='login'),
    path('registered', views.registeredView, name='registered'),
    path('logout', views.logoutView, name='logout'),
    path('home',views.home,name="home"),

]
