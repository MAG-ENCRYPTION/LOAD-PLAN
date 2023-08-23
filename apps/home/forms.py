from django import forms
from django.forms import inlineformset_factory
from .models import Charge, Semaine

ChargeFormSet = inlineformset_factory(Semaine, Charge, fields=('charge',), extra=len(Semaine.objects.all()))