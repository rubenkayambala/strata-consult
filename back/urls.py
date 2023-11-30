from django.urls import path
from .views import Dashboard, Users, Formations, Commandes, Emplois

app_name = 'back'

urlpatterns = [
    path('', Dashboard, name='dashboard'),
    path('users/', Users, name='users'),
    path('formations/', Formations, name='formations'),
    path('commandes/', Commandes, name='commandes'),
    path('emplois/', Emplois, name='emplois'),
]
