from django.contrib import admin
from django.urls import path

from fire.views import HomePageView, ChartView, PieCountbySeverity, LineCountbyMonth, MultilineIncidentTop3Country, multipleBarbySeverity
from fire import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('dashboard_chart', ChartView.as_view(), name='dashboard-chart'),
    path('chart/', PieCountbySeverity, name='chart'),
    path('multilineChart/', MultilineIncidentTop3Country, name='chart'),
    path('multiBarChart/', multipleBarbySeverity, name='chart'),
    path('stations', views.map_station, name='map-station'),

    path('locationlist', views.LocationList.as_view(), name='location-list'),
    path('locationlist/add', views.LocationCreateView.as_view(), name='location-add'),
    path('locationlist/<pk>', views.LocationUpdateView.as_view(), name='location-update'),
    path('locationlist/<pk>/delete', views.LocationDeleteView.as_view(), name='location-delete'),

    path('weatherconlist', views.WeatherConditionList.as_view(), name='weathercon-list'),
    path('weatherconlist/add', views.WeatherConditionCreateView.as_view(), name='weathercon-add'),
    path('weatherconlist/<pk>', views.WeatherConditionUpdateView.as_view(), name='weathercon-update'),
    path('weatherconlist/<pk>/delete', views.WeatherConditionDeleteView.as_view(), name='weathercon-delete'),

    path('incidents', views.map_incident, name='map-incident'),

    path('incidentlist', views.IncidentList.as_view(), name='incident-list'),
    path('incidentlist/add', views.IncidentCreateView.as_view(), name='incident-add'),
    path('incidentlist/<pk>', views.IncidentUpdateView.as_view(), name='incident-update'),
    path('incidentlist/<pk>/delete', views.IncidentDeleteView.as_view(), name='incident-delete'),

    path('firestatlist', views.FireStationList.as_view(), name='firestat-list'),
    path('firestatlist/add', views.FireStationCreateView.as_view(), name='firestat-add'),
    path('firestatlist/<pk>', views.FireStationUpdateView.as_view(), name='firestat-update'),
    path('firestatlist/<pk>/delete', views.FireStationDeleteView.as_view(), name='firestat-delete'),

    path('firefighterlist', views.FireFighterList.as_view(), name='firefighter-list'),
    path('firefighterlist/add', views.FireFighterCreateView.as_view(), name='firefighter-add'),
    path('firefighterlist/<pk>', views.FireFighterUpdateView.as_view(), name='firefighter-update'),
    path('firefighterlist/<pk>/delete', views.FireFighterDeleteView.as_view(), name='firefighter-delete'),

    path('firetrucklist', views.FireTruckList.as_view(), name='firetruck-list'),
    path('firetrucklist/add', views.FireTruckCreateView.as_view(), name='firetruck-add'),
    path('firetrucklist/<pk>', views.FireTruckUpdateView.as_view(), name='firetruck-update'),
    path('firetrucklist/<pk>/delete', views.FireTruckDeleteView.as_view(), name='firetruck-delete'),

]
