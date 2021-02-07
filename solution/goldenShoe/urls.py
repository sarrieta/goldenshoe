from django.urls import path

from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from solution import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('men/', views.men, name='men'),
    path('women/', views.women, name='women'),
    path('tracking/', views.tracking, name='tracking'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('about_us/', views.about_us, name='about_us'),
    path('get_cart/', views.get_cart, name='get_cart'),
    path('FAQ/', views.FAQ, name='FAQ'),
    path('add_to_cart/<int:product_id>/<int:quantity>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
