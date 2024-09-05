from django.urls import path

from plat.views.plat_views import modifier_plat, plat_create, plat_list, supprimer_plat



app_name= 'plat'

urlpatterns =[
    path('', plat_list, name='platlist'),
    path('ajouterplat/', plat_create, name='ajouterplat'),
    path('modifierplat/<int:id>/', modifier_plat, name='modifierplat'),
    path('supprimerplat/<int:id>/', supprimer_plat, name='supprimerplat'),
]