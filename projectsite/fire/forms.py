from django.forms import ModelForm, DateTimeInput
from django import forms
from fire.models import Locations, WeatherConditions, Incident, FireStation

class LocationForm(ModelForm):
    class Meta:
        model = Locations
        fields = "__all__"
        labels = {
            'name': 'Location Name',  
            'latitude': 'Latitude',  
            'longitude': 'Longitude',
            'address': 'Address',
            'city': 'City',
            'country': 'Country',
        }

class WeatherConditionForm(ModelForm):
    class Meta:
        model = WeatherConditions
        fields = "__all__"
        labels = {
            'incident': 'Incident',  
            'temperature': 'Temperature',  
            'humidity': 'Humidity',
            'wind_speed': 'Wind Speed',
            'weather_description': 'Weather Description',
        }

class IncidentForm(ModelForm):
    date_time = forms.DateTimeField(
        widget=DateTimeInput(attrs={
            'type': 'datetime-local',
            'class': 'form-control',  # You can add any class you need for styling
            'placeholder': 'Select Date and Time',
        })
    )
    class Meta:
        model = Incident
        fields = "__all__"
        labels = {
            'location': 'Location',  
            'date_time': 'Date Time',  
            'severity_level': 'Severity Level',
            'description': 'Description',
        }

class FireStationForm(ModelForm):
    class Meta:
        model = FireStation
        fields = "__all__"
        labels = {
            'name': 'Fire Station Name',  
            'latitude': 'Latitude',  
            'longitude': 'Longitude',
            'address': 'Address',
            'city': 'City',
            'country': 'Country',
        }