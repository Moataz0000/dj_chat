from django.urls import path
from . import views



urlpatterns = [
    path('',views.home, name='home'),
    path('home/',views.home, name='home'),
    path('sign-up/', views.sign_up, name='sign_up'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout , name='logout'),
]

