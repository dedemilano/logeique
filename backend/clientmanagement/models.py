from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client')
    noms = models.CharField(max_length=100)
    contact = models.CharField(max_length=50)
    avatar = models.ImageField(null=True, blank=True, upload_to="img/avatars/", default="img/avatars/default-user-img.png")

    class Meta():
        ordering = ['user', 'contact']

    def __str__(self):
        return f"{self.user.email}"

    def statuLogeique(self):
        return f"Client"
    
class Proposal(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="proposals")
    loyer_du_client = models.BigIntegerField(null=True)
    cotion_du_client = models.BigIntegerField(null=True)
    type_du_client = models.CharField(max_length=50, null=True, default=None)
    nombre_piece_desire = models.IntegerField(null=True, default=None)
    zone_desire = models.CharField(max_length=50, null=True, default=None)
    ville_desire = models.CharField(max_length=50, null=True, default=None)
    ajoute_le = models.DateField(auto_now_add=True)
    edite_le = models.DateField(auto_now=True)

    class Meta():
        ordering = ['client', 'loyer_du_client', 'cotion_du_client']

    def __str__(self):
        return f"{self.id} - {self.client}"
