# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('map/', views.map, name='map'),
    path('excel_file/', views.excel_download, name='download'),
    path('profile/', views.profile, name='profile'),
    path('table/', views.table, name='table'),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),
    # re_path(r'^(?!test/).*$', views.pages, name='pages') # Toutes les autres instances de liens seront redirigées
    # vers le login sauf pour le lien 'test/'

]
