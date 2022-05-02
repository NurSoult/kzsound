from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('top5', views.top5, name='top5'),
    path('contacts', views.contacts, name='contacts'),
    path('rappers', views.rappers, name='rappers'),
    path('sponsors', views.sponsors, name='sponsors'),
    path('email', views.subscribe, name='email')
]
