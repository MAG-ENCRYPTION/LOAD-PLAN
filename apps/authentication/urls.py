# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path

from . import views
from .views import login_view, register_user, reset_password
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('login/reset', reset_password, name='reset'),
    path('login/reset/verify_code_password', views.verify_code, name='confirm'),
    path('login/reset/verify_code_password/validation', views.validation, name='validation'),
]
