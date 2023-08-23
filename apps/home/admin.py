# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from .models import *

from django.contrib import admin


class SemaineAdmin(admin.ModelAdmin):
    list_display = ('number', 'year', 'start', 'end')


class EntiteAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'localization')


class ActivityAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'type', 'start', 'end', 'foreverybody')


class AuditAdmin(admin.ModelAdmin):
    list_display = ('id_user', 'action')


class ChargeAdmin(admin.ModelAdmin):
    list_display = ('code_activity', 'id_user', 'id_semaine', 'charge')


class EntityActivityAdmin(admin.ModelAdmin):
    list_display = ('code_activity', 'code_entity')


class ParentAdmin(admin.ModelAdmin):
    list_display = ('racine', 'parent')


class EntityUSerAdmin(admin.ModelAdmin):
    list_display = ('entity', 'utilisateur')


class ActivityUSerAdmin(admin.ModelAdmin):
    list_display = ('activity', 'utilisateur')


class ProjetFermeAdmin(admin.ModelAdmin):
    list_display = ('nomProjet', 'dateFemeture')


admin.site.register(ProjectFerme, ProjetFermeAdmin)
admin.site.register(Semaine, SemaineAdmin)
admin.site.register(Entite, EntiteAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Audit, AuditAdmin)
admin.site.register(Charge, ChargeAdmin)
admin.site.register(EntityActivity, EntityActivityAdmin)
admin.site.register(EntityUSer, EntityUSerAdmin)
admin.site.register(ActivityUSer, ActivityUSerAdmin)
