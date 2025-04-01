from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User

from models import Client, Proposal
from serializers import ClientSerializer, ProposalSerializer

from models import House
from serializers import HouseSerializer

class AllClients(APIView):

     def get(self, request):
        try:
            query = Client.objects.all().order_by('-id')
            serializer = ClientSerializer(query, many=True)
            return Response(serializer.data)
        except AssertionError as e:
            response_msg = {'error': True, 'type: ': str(e)}
        return Response(response_msg)

class GetClient(APIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly]

    def post(self, request):
        try:
            query = Client.objects.get(user=request.user)
            serializer = ClientSerializer(query)
            return Response(serializer.data)
        except AssertionError as e:
            response_msg = {'error': True, 'type: ': str(e)}
        return Response(response_msg)

class GetHousesProposals(APIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly]

    def post(self, request):
        try:
            query = Proposal.objects.all().order_by('-id')
            serializer = ProposalSerializer(query, many=True)
            return Response(serializer.data)
        except AssertionError as e:
            response_msg = {'error': True, 'type: ': str(e)}
        return Response(response_msg)

class AllProposals(APIView):

    def get(self, request):
        try:
            query = Proposal.objects.all().order_by('-id')
            serializer = ProposalSerializer(query, many=True)
            return Response(serializer.data)
        except AssertionError as e:
            response_msg = {'error': True, 'type: ': str(e)}
        return Response(response_msg)

#   RECUPERATION / LISTE DES PROPOSITIONS OU DEMANDES D'UN SEUL CLIENT
class ClientProposals(APIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly]

    def post(self, request):
        try:
            client = Client.objects.get(user=request.user)
            query = Proposal.objects.filter(client=client).order_by('-id')
            serializer = ProposalSerializer(query, many=True)
            return Response(serializer.data)

        except AssertionError as e:
            response_msg = {'error': True, 'type: ': str(e)}
            return Response(response_msg)

#   AJOUT D'UNE NOUVELLE PROPOSITION OU DEMANDE
class AddClientProposal(APIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly]

    def post(self, request):
        try:
            data = request.data
            user = User.objects.get(id=request.user.id)
            client = Client.objects.get(user=user)
            noms = f"{str(user.last_name).upper()} {str(user.first_name)}"
            Proposal.objects.create(
                client=client,
                ville_desire=data['ville'],
                zone_desire=data['zone'],
                loyer_du_client=data['loyer'],
                cotion_du_client=data['cotion'],
                type_du_client=data['type'],
                nombre_piece_desire=data['piece']
            )
            response_msg = {'error': False, 'status': 200}
        except AssertionError as e:
            response_msg = {'error': True, 'type: ': str(e)}
        return Response(response_msg)

#   EDITION D'UNE PROPOSITION OU DEMANDE EXISTANTE
class EditProposal(APIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly]

    def put(self, request, id):
        try:
            data = request.data
            proposal = Proposal.objects.get(id=id)
            proposal.loyer_du_client=data['loyer']
            proposal.cotion_du_client=data['cotion']
            proposal.type_du_client=data['type_maison']
            proposal.nombre_piece_desire=data['nombre_piece']
            proposal.zone_desire=data['quartier']
            proposal.ville_desire=data['ville']
            proposal.save()
            response_msg = {'error': False}
        except AssertionError as e:
            response_msg = {'error': True, 'type: ': str(e)}
        return Response(response_msg)

#   SUPRESSION D'UNE PROPOSITION OU DEMANDE EXISTANTE
class DeleteProposal(APIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly]

    def delete(self, request, id):
        try:
            proposal = Proposal.objects.get(id=id)
            proposal.delete()
            response_msg = {'error': False}
        except AssertionError as e:
            response_msg = {'error': True, 'type: ': str(e)}
        return Response(response_msg)

class ProposedHouses(APIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly]

    def get(self, request):
        query = House.objects.all().order_by('-id')
        serializer = HouseSerializer(query, many=True)
        return Response(serializer.data)
