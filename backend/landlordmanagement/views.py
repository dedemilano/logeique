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


    

class AddHouse(APIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly]

    def post(self, request, *args, **kwargs):
        response_msg = {}
        try:
            user = User.objects.get(id=request.user.id)
            landlord = Landlord.objects.get(user=request.user)
            quan_dispo = 1
            noms = f"{str(user.last_name).upper()} {str(user.first_name)}"

            if quan_dispo <= 1:
                if request.data['radio'] == 'location':
                    maison, created = House.objects.get_or_create(
                        landlord=landlord,
                        ville=request.data['ville'],
                        quartier=request.data['quartier'],
                        loyer=request.data['loyer'],
                        cotion=request.data['cotion'],
                        type_maison=request.data['type'],
                        piece=request.data['piece'],
                        location=True,
                        vente=False,
                        image=request.FILES['image'],
                        #classe=getClasseMaison(int(request.data['loyer']))
                    )

                    maison.refresh_from_db()

                    images = request.FILES.getlist('images')
                    for image in images:
                        maison_images = HouseImages.objects.create(
                            maison = maison,
                            image = image
                        )
                        #maison = MaisonSerializer(maison)
                        response_msg = {'error': False, 'status': 200}
                elif request.data['radio'] == 'vente':
                    maison, created = House.objects.get_or_create(
                        landlord=landlord,
                        ville=request.data['ville'],
                        quartier=request.data['quartier'],
                        loyer=request.data['loyer'],
                        cotion=request.data['cotion'],
                        type_maison=request.data['type'],
                        piece=request.data['piece'],
                        location=False,
                        vente=True,
                        image=request.FILES['image'],
                        #classe=getClasseMaison(int(request.data['loyer']))
                    )

                    maison.refresh_from_db()

                    images = request.FILES.getlist('images')
                    for image in images:
                        maison_images = HouseImages.objects.create(
                            maison = maison,
                            image = image
                        )
                        
                        response_msg = {'error': False, 'status': 200}

                elif request.data['radio'] == 'location_vente':
                    maison, created = House.objects.get_or_create(
                        landlord=landlord,
                        ville=request.data['ville'],
                        quartier=request.data['quartier'],
                        loyer=request.data['loyer'],
                        cotion=request.data['cotion'],
                        type_maison=request.data['type'],
                        piece=request.data['piece'],
                        location=True,
                        vente=True,
                        image=request.FILES['image'],
                        #classe=getClasseMaison(int(request.data['loyer']))
                    )

                    maison.refresh_from_db()
                    
                    images = request.FILES.getlist('images')
                    for image in images:
                        maison_images = HouseImages.objects.create(
                            maison = maison,
                            image = image
                        )
                        
                        response_msg = {'error': False, 'status': 200}
            elif quan_dispo > 1:
                if loc_ven == 1:
                    House.objects.create(
                        landlord=landlord,
                        ville=request.data['ville'],
                        quartier=request.data['quartier'],
                        loyer=request.data['loyer'],
                        cotion=request.data['cotion'],
                        type_maison=request.data['type'],
                        nombre_piece=request.data['piece'],
                        en_location=True,
                        en_vente=False,
                        image=request.data['image'],
                        classe=getClasseMaison(int(request.data['loyer'])),
                        quantite=quan_dispo
                    )

                elif loc_ven == 2:
                    House.objects.create(
                        landlord=landlord,
                        ville=request.data['ville'],
                        quartier=request.data['quartier'],
                        loyer=request.data['loyer'],
                        cotion=request.data['cotion'],
                        type_maison=request.data['type'],
                        nombre_piece=request.data['piece'],
                        en_location=False,
                        en_vente=True,
                        image=request.data['image'],
                        classe=getClasseMaison(int(request.data['loyer'])),
                        quantite=quan_dispo
                    )

                elif loc_ven == 3:
                    House.objects.create(
                        landlord=landlord,
                        ville=request.data['ville'],
                        quartier=request.data['quartier'],
                        loyer=request.data['loyer'],
                        cotion=request.data['cotion'],
                        type_maison=request.data['type'],
                        nombre_piece=request.data['piece'],
                        en_location=True,
                        en_vente=True,
                        image=request.data['image'],
                        classe=getClasseMaison(int(request.data['loyer'])),
                        quantite=quan_dispo
                    )
        except AssertionError as e:
            response_msg = {'error': True, 'type: ': str(e)}
        return Response(response_msg)


class EditeMaison(APIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly]
    #parser_class = (FileUploadParser,)

    def put(self, request, id):
        try:
            data = request.data
            maison = House.objects.get(id=id)
            loc_ven = data['loc_ven']
            quan_dispo = int(data['quan_dispo'])
            print(data['image'])

            if quan_dispo <= 1:
                if loc_ven == 1:
                    maison.ville = data['ville']
                    maison.quartier = data['quartier']
                    maison.loyer = data['loyer']
                    maison.cotion = data['cotion']
                    maison.type_maison = data['type_maison']
                    maison.nombre_piece = data['nombre_piece']
                    maison.en_location = True
                    maison.en_vente = False
                    maison.image = data['image']
                    maison.classe = getClasseMaison(int(data['loyer']))
                    maison.save()
                
                elif loc_ven == 2:
                    maison.ville = data['ville']
                    maison.quartier = data['quartier']
                    maison.loyer = data['loyer']
                    maison.cotion = data['cotion']
                    maison.type_maison = data['type_maison']
                    maison.nombre_piece = data['nombre_piece']
                    maison.en_location = False
                    maison.en_vente = True
                    maison.image = data['image']
                    maison.classe = getClasseMaison(int(data['loyer']))
                    maison.save()

                elif loc_ven == 3:
                    maison.ville = data['ville']
                    maison.quartier = data['quartier']
                    maison.loyer = data['loyer']
                    maison.cotion = data['cotion']
                    maison.type_maison = data['type_maison']
                    maison.nombre_piece = data['nombre_piece']
                    maison.en_location = True
                    maison.en_vente = True
                    maison.image = data['image']
                    maison.classe = getClasseMaison(int(data['loyer']))
                    maison.save()

            elif quan_dispo > 1:
                if loc_ven == 1:
                    maison.ville = data['ville']
                    maison.quartier = data['quartier']
                    maison.loyer = data['loyer']
                    maison.cotion = data['cotion']
                    maison.type_maison = data['type_maison']
                    maison.nombre_piece = data['nombre_piece']
                    maison.en_location = True
                    maison.en_vente = False
                    maison.image = data['image']
                    maison.quantite = quan_dispo
                    maison.classe = getClasseMaison(int(data['loyer']))
                    maison.save()
                
                elif loc_ven == 2:
                    maison.ville = data['ville']
                    maison.quartier = data['quartier']
                    maison.loyer = data['loyer']
                    maison.cotion = data['cotion']
                    maison.type_maison = data['type_maison']
                    maison.nombre_piece = data['nombre_piece']
                    maison.en_location = False
                    maison.en_vente = True
                    maison.image = data['image']
                    maison.quantite = quan_dispo
                    maison.classe = getClasseMaison(int(data['loyer']))
                    maison.save()

                elif loc_ven == 3:
                    maison.ville = data['ville']
                    maison.quartier = data['quartier']
                    maison.loyer = data['loyer']
                    maison.cotion = data['cotion']
                    maison.type_maison = data['type_maison']
                    maison.nombre_piece = data['nombre_piece']
                    maison.en_location = True
                    maison.en_vente = True
                    maison.image = data['image']
                    maison.quantite = quan_dispo
                    maison.classe = getClasseMaison(int(data['loyer']))
                    maison.save()
            response_msg = {'error': False}
        except AssertionError as e:
            response_msg = {'error': True, 'type: ': str(e)}
        return Response(response_msg)

class DeleteHouse(APIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly]

    def delete(self, request, id):
        try:
            maison = House.objects.get(id=id)
            maison.delete()
            response_msg = {'error': False}
        except AssertionError as e:
            response_msg = {'error': True, 'type: ': str(e)}
        return Response(response_msg)







