from unittest.util import _MAX_LENGTH
from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact = models.CharField(max_length=100)

    class Meta:
        db_table="tblemployee"


#class Client(models.Model):
#    name=models.CharField(max_length=100)
#    email=models.EmailField()
#    def __str__(self):
#        return self.nom

#class Commande(models.Model):
#    client=models.ForeignKey(Client, on_delete=models.CASCADE)
#    date = models.DateField()
#    montant = models.DecimalField(max_digits=8,decimal_places=2)
#
#    def __str__(self):
#        return self.date.strftime('%Y-%m-%d') + " - " + self.client.nom


class Paiement(models.Model):
    totalPaye = models.FloatField()
    montantPaye = models.FloatField()
    class Meta:
        db_table="Paiement"
   

class Facture(models.Model):
    paiement = models.ForeignKey(Paiement, on_delete=models.CASCADE, null=True)
    nbrJours = models.FloatField()
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    montant = models.FloatField()
    class Meta:
        db_table="Facture"
   

class Medcine(models.Model):
    nom=models.CharField(max_length=100)
    prenom=models.CharField(max_length=100)
    specialite=models.CharField(max_length=100)

    def __str__(self):
        return self.nom
    class Meta:
        db_table="Medcine"

class Patient(models.Model):
    nom=models.CharField(max_length=100)
    prenom=models.CharField(max_length=100)
    dateNaissance=models.DateField()
    malade=models.CharField(max_length=100)
    doctor=models.ManyToManyField(Medcine,through='Consulter')

    def __str__(self):
        return self.nom
    class Meta:
        db_table="Patient"

class Consulter(models.Model):
    medcine = models.ForeignKey(Medcine, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    voir=models.CharField(max_length=100)
    def __str__(self):
        return "{}_{}".format(self.patient.__str__(), self.medcine.__str__())
    class Meta:
        db_table="Consulter"


class RendezVous(models.Model):
    date=models.DateField()
    heure_debut=models.IntegerField()
    heure_fin=models.IntegerField()
    medcine = models.ForeignKey(Medcine, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)


class Personne(models.Model):
    Nom = models.CharField(max_length=100)
    PRENOM = models.CharField(max_length=100)
    CIN = models.CharField(max_length=100)
    class Meta:
        abstract = True

class ClientLocation(Personne):
    Adresse = models.CharField(max_length=100)
    Telephone = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Num_assurance = models.CharField(max_length=100)
    class Meta:
        db_table="ClientLocation"

