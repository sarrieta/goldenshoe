from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #signup 
    path('signup/', views.signup, name='signup'),
    #register
    path('register/', views.register, name='register'),
    #user profile edit page 
    path('profile/', views.profile, name='profile'),
    #login page
    path('login/', views.login, name='login'),
    #logout page
    path('logout/', views.logout, name = 'logout'),
    #similar hobbies
    path('similarHobbies/', views.similarHobbies, name='similarHobbies'),
    #Ajax: filter 
    path('filter/', views.filter, name='filter'),
    #upload image
    path('uploadimage/', views.upload_image, name='uploadimage'),
]