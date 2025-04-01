from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'normalauthentication'
urlpatterns = [
    path('register/', RegisterNow.as_view()),
    path('login-authtoken/', obtain_auth_token),
    path('login/', LoginView.as_view()),
    path('userToken/', UserStatus.as_view()),
    path('a-user/', GetUser.as_view()),
    
]