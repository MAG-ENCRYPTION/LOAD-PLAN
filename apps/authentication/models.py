# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models


class ForgottenPasswordMailling(models.Model):
    id = models.AutoField(primary_key=True)
    ForgotMail = models.CharField(max_length=100)
