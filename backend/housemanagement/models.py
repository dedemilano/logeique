from django.db import models
from landlordmanagement.models import Landlord

# Create your models here.

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)


class House(models.Model):
    ville = models.CharField(max_length=100)
    quartier = models.CharField(max_length=100)
    loyer = models.BigIntegerField()
    cotion = models.BigIntegerField()
    type_maison = models.CharField(max_length=200)
    piece = models.IntegerField()
    location = models.BooleanField(default=False, null=True, blank=True)
    vente = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="img/maisons/")
    ajoute_le = models.DateField(auto_now_add=True)
    edite_le = models.DateField(auto_now=True)
    #occupants = models.IntegerField(default=1, null=True, blank=True)
    quantite = models.IntegerField(default=1, null=True, blank=True)
    #classe = models.CharField(max_length=7)
    landlord = models.ForeignKey(Landlord, on_delete=models.CASCADE, related_name="maisons")

    def __str__(self):
        return f"Ville: {self.ville} - Quartier: {self.quartier} - Loyer: {self.loyer}"
    

class HouseImages(models.Model):
    maison = models.ForeignKey(House, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(null=True, blank=True, upload_to="img/maisons/")

    def __str__(self):
        return f"Maison: {self.maison} - Image: {self.image}"