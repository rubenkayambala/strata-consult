from django.urls import path
from .views import Home, Search, BigSearch, Etude_sol, EmploiList, DetailEmploi, Appel, assistance_emploi, Immobilier, Achat, FormationList, DetailFormation, FollowFormation, UnfollowFormation, Contact, about

app_name = 'home'

urlpatterns = [
    path('', Home, name='home'),
    path('search/', Search, name='search'),
    path('searchs/', BigSearch, name='big-search'),
    path('etude_sol/', Etude_sol, name='etude_sol'),
    path('emploi/', EmploiList, name='emploi'),
    path('emploi_detail/<int:pk>/', DetailEmploi, name='detail_emploi'),
    path('appel_d_offre/', Appel, name='appel'),
    path('immobilier/', Immobilier, name='immobilier'),
    path('achat/', Achat, name='achat'),
    path('assistance_emploi/', assistance_emploi, name='assistance_emploi'),
    path('formations/', FormationList, name='formation'),
    path('formation/<str:slug>/', DetailFormation, name='detail_formation'),
    path('Followformation/<str:slug>/', FollowFormation, name='follow_formation'),
    path('Unfollowformation/<str:slug>/', UnfollowFormation, name='unfollow_formation'),
    path('contact/', Contact, name='contact'),
    path('about/', about, name='about'),
]
