from unicodedata import name
from django.urls import path

from base import views
from . import urls

urlpatterns =[
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('logout/', views.logoutPage, name='logout'),
    path('login/', views.loginPage, name='login'),
    path('details/', views.details, name="details"),
    path('store/', views.store, name='store'),
]