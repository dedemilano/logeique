from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication

from models import *
from serializers import *
from django.contrib.auth.models import User


# Create your views here.

class AllLandlords(APIView):

     def get(self, request):
        try:
            query = Landlord.objects.all().order_by('-id')
            serializer = LandlordSerializer(query, many=True)
            return Response(serializer.data)
        except AssertionError as e:
            response_msg = {'error': True, 'type: ': str(e)}
            return Response(response_msg)


class GetLandlord(APIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly]

    def post(self, request):
        try:
            #user = User.objects.get(auth_token=request.data['token'])
            landlord = Landlord.objects.get(user=request.user)
            serializer = LandlordSerializer(landlord)
            return Response(serializer.data)
        except AssertionError as e:
            response_msg = {'error': True, 'type: ': str(e)}
        return Response(response_msg)


class AllHouses(APIView):

    def get(self, request):
        query = House.objects.all().order_by('-id')
        serializer = HouseSerializer(query, many=True)
        return Response(serializer.data)


class LandlordHouses(APIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly]
    
    def post(self, request):
        try:
            landlord = Landlord.objects.get(user=request.user)
            query = House.objects.filter(landlord=landlord).order_by('-id')
            serializer = HouseSerializer(query, many=True)
            return Response(serializer.data)
        except AssertionError as e:
            response_msg = {'error': True, 'type: ': str(e)}
            return Response(response_msg)


    











