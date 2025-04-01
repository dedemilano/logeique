from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'housemanagement'
urlpatterns = [
path('all-maisons/', AllHouses.as_view()),
path('add-maison/', AddHouse.as_view()),
path('edit-maison/<int:id>/', EditHouse.as_view()),
path('delete-maison/<int:id>/', DeleteHouse.as_view()),
    
]