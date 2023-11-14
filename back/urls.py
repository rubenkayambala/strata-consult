from django.urls import path
from .views import Dashboard, Users, Formations

app_name = 'back'

urlpatterns = [
    path('', Dashboard, name='dashboard'),
    path('users/', Users, name='users'),
    path('formations/', Formations, name='formations'),
]
