from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'normalauthentication'
urlpatterns = [
    path('login/',LoginView.as_view(),name='login'),
    
]