from unittest.util import _MAX_LENGTH
from django.db import models


class Personne(models.Model):
    Nom = models.CharField(max_length=100)
    PRENOM = models.CharField(max_length=100)
    CIN = models.CharField(max_length=100)
    Telephone = models.CharField(max_length=100)
    Adresse = models.CharField(max_length=100)
    class Meta:
        abstract = True



class Employe(Personne):
    Num_couverture = models.CharField(max_length=100)
    Salaire = models.FloatField()
    class Meta:
        db_table="Employe"

class Agence(models.Model):
    Nom = models.CharField(max_length=100)
    Telephone = models.CharField(max_length=100)
    IF = models.CharField(max_length=100)
    ICE = models.CharField(max_length=100)
    class Meta:
        db_table="Agence"
    def __str__(self):
        return self.Nom

class Voiture(models.Model):
    Nom = models.CharField(max_length=100)
    Mileage = models.CharField(max_length=100)
    Transmission = models.CharField(max_length=100)
    Fuel = models.CharField(max_length=100)
    Luggage = models.CharField(max_length=100)
    Matricule = models.CharField(max_length=100)
    Marque = models.CharField(max_length=100)
    Modele = models.CharField(max_length=100)
    Annee = models.IntegerField()
    NbPlaces = models.IntegerField()
    Couleur = models.CharField(max_length=100)
    PrixParJour = models.FloatField()
    IsAvailable = models.BooleanField()
    Image = models.ImageField(null=False,blank = False, upload_to="images/")
    Agence = models.ForeignKey(Agence, on_delete=models.CASCADE)

    class Meta:
        db_table="Voiture"

class Reservation(models.Model):
    car = models.ForeignKey(Voiture, on_delete=models.CASCADE)
    pickup_location = models.CharField(max_length=100)
    dropoff_location = models.CharField(max_length=100)
    pickup_date = models.DateField()
    dropoff_date = models.DateField()
    pickup_time = models.CharField(max_length=100)

    def __str__(self):
        return f"Reservation #{self.pk}"

    class Meta:
        db_table = "Reservation"


class Reservation2(models.Model):
    DateRes = models.DateField()
    DateDebut = models.DateField()
    DateFin = models.DateField()
    Employe = models.ForeignKey(Employe, on_delete=models.CASCADE)
    Voiture = models.OneToOneField(Voiture,on_delete=models.CASCADE)

    class Meta:
        db_table="Reservation2"

class Client(Personne):
    Email = models.CharField(max_length=100)
    Num_assurance = models.CharField(max_length=100)
    Reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    class Meta:
        db_table="Client"

