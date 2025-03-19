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


#   CREATION DE COMPTE UTILISATEUR LOGEIQUE
class RegisterNow(APIView):
    def post(self, request):
        #print(request.data)
        data = {
            'username': request.data['contact'],
            'email': str(request.data['email']).lower(),
            'password': request.data['password_v'],
            'first_name': request.data['first_name'],
            'last_name': str(request.data['last_name']).upper()
        }
        status = request.data['statu']
        noms = f"{str(request.data['last_name']).upper()} {str(request.data['first_name'])}"
        serializers = UserSerializers(data=data)
        
        if serializers.is_valid():
            serializers.save()
            if int(status) == 1:
                landlord_user = User.objects.get(username=request.data['contact'])
                Landlord.objects.create(
                    user=landlord_user,
                    noms=noms,
                    contact=request.data['contact']
                )
                return Response({'error': False, 'isRegistered': True, 'status': int(status)})
            elif int(status) == 2:
                client_user = User.objects.get(username=request.data['contact'])
                Client.objects.create(
                    user=client_user,
                    noms=noms,
                    contact=request.data['contact']
                )
                return Response({'error': False, 'isRegistered': True, 'status': int(status)})
            return Response({'error': True, 'isRegistered': False})
        print(serializers.errors)
        return Response({'error': True, 'isRegistered': False})


class UserStatus(APIView):
    permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication, ]

    def post(self, request):
        print(f"Token: {request.data['token']}")
        try:
            user = User.objects.get(auth_token=request.data['token'])
            print(f"User: {user}")
            try:
                user.landlord
                status = 1
            except:
                user.client
                status = 2
            response_msg = {'error': False, 'status': int(status)}
        except AssertionError as e:
            response_msg = {'error': True, 'type: ': str(e)}
        return Response(response_msg)
