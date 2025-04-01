from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'landlordmanagement'
urlpatterns = [
path('all-landlords/', AllLandlords.as_view()),
path('a-landlord/', GetLandlord.as_view()),
path('landlord-maisons/', LandlordHouses.as_view()),
    
]