# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.contrib.auth import admin
from django.contrib.auth.models import User
from django.urls import path, include  # add this
from django.http import HttpResponse
from io import BytesIO
from reportlab.pdfgen import canvas
from apps.home import views

urlpatterns = [
    path('admin/', admin.admin.site.urls, name='admin'),          # Django admin route
    path("", include("apps.authentication.urls")),  # Auth routes - login / register
    path("", include("apps.home.urls")),       # UI Kits Html files

]
