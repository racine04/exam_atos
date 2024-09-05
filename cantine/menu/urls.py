from django.urls import path

from menu.views.menu_views import menu_create, menu_list, modifier_menu, supprimer_menu


app_name= 'menu'

urlpatterns =[
    path('', menu_list, name='menulist'),
    path('ajoutermenu/', menu_create, name='ajoutermenu'),
    path('modifiermenu/<int:id>/', modifier_menu, name='modifiermenu'),
    path('supprimermenu/<int:id>/', supprimer_menu, name='supprimermenu'),
]