from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from .serializers import UserSerializers


# Vue pour la connexion (obtention des tokens JWT)
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return Response({'error': False, } , status=status.HTTP_200_OK)
            
        return Response({'error': 'Identifiants invalides'}, status=status.HTTP_401_UNAUTHORIZED)