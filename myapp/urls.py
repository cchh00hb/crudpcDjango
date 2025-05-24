from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('pcs/', views.liste_pcs, name='liste_pcs'),
    path('pc/ajouter/', views.ajouter_pc, name='ajouter_pc'),
    path('pc/<int:pc_id>/', views.detail_pc, name='detail_pc'),
    path('pc/<int:pc_id>/modifier/', views.modifier_pc, name='modifier_pc'),
    path('pc/<int:pc_id>/supprimer/', views.supprimer_pc, name='supprimer_pc'),
    path('pc/<int:pc_id>/ajouter_composant/', views.ajouter_composant, name='ajouter_composant'),
]
