from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #signup 
    path('signup/', views.signup, name='signup'),
    #register
    path('register/', views.register, name='register'),
    #login page
    path('login/', views.login, name='login'),
]