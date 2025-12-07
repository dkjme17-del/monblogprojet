# blogapp/urls.py (NOUVEAU FICHIER) 
from django.urls import path 

from . import views # On importera nos vues d'ici 
app_name = 'blogapp' # C'est une bonne pratique pour nommer vos URLs 
urlpatterns = [ 
   path('', views.accueil_view, name='accueil'), 
   path('inscription/', views.inscription_view, name='inscription'), 
   path('connexion/', views.connexion_view, name='connexion'), # URL pour la connexion 
   path('deconnexion/', views.deconnexion_view, name='deconnexion'), # URL pour la deconnexion 
      # URLs pour les articles 
   path('article/creer/', views.creer_article_view, name='creer_article'), 
   path('article/<int:pk>/', views.detail_article_view, name='detail_article'), # pk est un entier (int) 
   path('article/<int:pk>/modifier/', views.modifier_article_view, name='modifier_article'), 
   path('article/<int:pk>/supprimer/', views.supprimer_article_view, name='supprimer_article'),
   path('article/<int:article_pk>/ajouter_commentaire/', views.ajouter_commentaire_view, name='ajouter_commentaire'),
   path('profil/<str:username>/', views.profil_utilisateur_view, name='profil_utilisateur'), 

]