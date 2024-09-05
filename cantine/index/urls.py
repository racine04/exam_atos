from django.urls import path

from index.views.index_views import index


app_name= 'index'

urlpatterns =[
    path('', index, name='acceuil'),
]