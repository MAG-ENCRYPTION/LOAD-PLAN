from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django import template

register = template.Library()


def DateFormate(DateDuJour):
    if DateDuJour.month.__int__() < 10 and DateDuJour.day.__int__() < 10:
        cejour = f'{DateDuJour.year}-0{DateDuJour.month}-0{DateDuJour.day}'
    elif DateDuJour.day.__int__() < 10:
        cejour = f'{DateDuJour.year}-{DateDuJour.month}-0{DateDuJour.day}'
    elif DateDuJour.month.__int__() < 10:
        cejour = f'{DateDuJour.year}-0{DateDuJour.month}-{DateDuJour.day}'
    else:
        cejour = f'{DateDuJour.year}-{DateDuJour.month}-{DateDuJour.day}'
    return cejour


class Semaine(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.IntegerField()
    year = models.IntegerField()
    start = models.DateTimeField()
    end = models.DateTimeField()

    def totaliser(self, userID):
        CHARGE = []
        charges = Charge.objects.filter(id_semaine_id=self.id, id_user_id=userID)
        for charge in charges:
            CHARGE.append(float(charge.charge))
        return sum(CHARGE)

    def debut(self):
        return DateFormate(self.start)

    def __str__(self):
        return f"Semaine : Sem {self.number} a partir de {self.start.day} / {self.start.month} / {self.start.year}"


class Cloturation(models.Model):
    id = models.AutoField(primary_key=True)
    SemaineClose = models.ForeignKey(Semaine, on_delete=models.CASCADE)

    def debut(self):
        return DateFormate(self.SemaineClose.start)

    def __str__(self):
        return f"{self.SemaineClose.start}"


class CloturationUSer(models.Model):
    id = models.AutoField(primary_key=True)
    SemaineClose = models.ForeignKey(Semaine, on_delete=models.CASCADE)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)

    def debut(self):
        return DateFormate(self.SemaineClose.start)

    def __str__(self):
        return f'Semaine {self.SemaineClose.start} Clos par {self.utilisateur.username}'


class ProjectFerme(models.Model):
    id = models.AutoField(primary_key=True)
    nomProjet = models.CharField(max_length=100)
    start = models.DateField(default=timezone.now().today())
    description = models.CharField(max_length=100, default="projet")
    dateFemeture = models.DateField(default=timezone.now().today())

    def __str__(self):
        return f'Projet {self.nomProjet} fermé le {self.dateFemeture}'


class WaitingProject(models.Model):
    id = models.AutoField(primary_key=True)
    nomProjet = models.CharField(max_length=100)
    start = models.DateField(default=timezone.now().today())
    description = models.CharField(max_length=100, default="projet")
    dateFemeture = models.DateField(default=timezone.now().today())
    motif = models.CharField(max_length=100)

    def __str__(self):
        return f'Projet {self.nomProjet} fermé le {self.dateFemeture}'


class Entite(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    localization = models.CharField(max_length=100)

    def __str__(self):
        if 'CCA' in self.code:
            return f'{self.name}'
        elif 'DSI' in self.code:
            return f'{self.name} (DSI)'


class Activity(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    type = models.CharField(max_length=10)
    start = models.DateField()
    end = models.DateField()
    foreverybody = models.IntegerField(db_column='ForEverybody', db_comment='Elle permet de signifier si une activitÚ '
                                                                            'concerne une seule personne ou pas. 0 si'
                                                                            ' elle concerne une seule personne et 1 '
                                                                            'sinon')  # Field name made lowercase.

    def __str__(self):
        return f'{self.name} ____ Type: {self.type}'


class Audit(models.Model):
    id = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=1)


class Charge(models.Model):
    id = models.AutoField(primary_key=True)
    code_activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    # code_entity = models.ForeignKey(Entite, on_delete=models.CASCADE)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_semaine = models.ForeignKey(Semaine, on_delete=models.CASCADE, default=1)
    charge = models.FloatField()
    insert_date = models.DateTimeField(default=timezone.now())
    modify_date = models.DateField()

    def debut(self):
        return DateFormate(self.id_semaine.start)

    def __str__(self):
        return f"""Utilisateur : {self.id_user.username}
          Activité : {self.code_activity.name} 
          Charge : {self.charge}
          Semaine : Sem {self.id_semaine.number} a partir de {self.id_semaine.start.day} / {self.id_semaine.start.month} / {self.id_semaine.start.year}
           """


class EntityActivity(models.Model):
    id = models.AutoField(primary_key=True)
    code_activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    code_entity = models.ForeignKey(Entite, on_delete=models.CASCADE)

    def __str__(self):
        return self.code_activity.name


class EntityUSer(models.Model):
    id = models.AutoField(primary_key=True)
    entity = models.ForeignKey(Entite, on_delete=models.CASCADE)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)


class ActivityUSer(models.Model):
    id = models.AutoField(primary_key=True)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)

    def total(self):
        CHARGE = []
        charges = Charge.objects.filter(code_activity_id=self.activity.id,
                                        id_user_id =self.utilisateur.id)
        for charge in charges:
            CHARGE.append(float(charge.charge))
        return sum(CHARGE)

