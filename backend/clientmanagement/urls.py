from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'clientmanagement'
urlpatterns = [
    path('all-clients/', AllClients.as_view()),
	path('a-client/', GetClient.as_view()),
    path('all-proposals/', AllProposals.as_view()),
    path('proposals/', ClientProposals.as_view()),
    path('add-proposal/', AddProposal.as_view()),
    path('edit-proposal/<int:id>/', EditProposal.as_view()),
    path('delete-proposal/<int:id>/', DeleteProposal.as_view()),
    
]