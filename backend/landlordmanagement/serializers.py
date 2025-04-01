from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

class LandlordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Landlord
        fields = "__all__"
        depth = 1

class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = "__all__"
        depth = 1

class HouseImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseImages
        fields = "__all__"
        depth = 1