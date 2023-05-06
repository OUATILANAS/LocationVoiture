from django import forms  
from app.models import Reservation, Voiture  
from app.models import Agence  
AVAILABLE= [
    ('0', '0'),
    ('1', '1'),
    ]
class VoitureForm(forms.ModelForm):  
    class Meta:  
        model = Voiture  
        fields = ['Nom', 'Mileage','Transmission', 'Fuel','Luggage', 'Matricule','Marque', 'Modele','Annee', 'NbPlaces','Couleur', 'PrixParJour','IsAvailable', 'Image', 'Agence'] 
        widgets = { 'Nom': forms.TextInput(attrs={ 'class': 'form-control' }),
        'Mileage': forms.TextInput(attrs={ 'class': 'form-control' }), 
        'Transmission': forms.TextInput(attrs={ 'class': 'form-control' }), 
        'Fuel': forms.TextInput(attrs={ 'class': 'form-control' }), 
        'Luggage': forms.TextInput(attrs={ 'class': 'form-control' }), 
        'Matricule': forms.TextInput(attrs={ 'class': 'form-control' }), 
        'Marque': forms.TextInput(attrs={ 'class': 'form-control' }), 
        'Modele': forms.TextInput(attrs={ 'class': 'form-control' }), 
        'Annee': forms.TextInput(attrs={ 'class': 'form-control' }), 
        'NbPlaces': forms.TextInput(attrs={ 'class': 'form-control' }),  
        'Couleur': forms.TextInput(attrs={ 'class': 'form-control' }),  
        'PrixParJour': forms.TextInput(attrs={ 'class': 'form-control' }),  
        'IsAvailable': forms.Select(choices=AVAILABLE,attrs={ 'class': 'form-control' }),  
            'Agence': forms.Select(attrs={ 'class': 'form-control' }),
                }
class ReservationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['car'].queryset = Voiture.objects.filter(IsAvailable=1)

    class Meta:
        model = Reservation
        fields = ['car', 'pickup_location', 'dropoff_location', 'pickup_date', 'dropoff_date', 'pickup_time']
