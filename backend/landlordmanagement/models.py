from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Landlord(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='landlord')
    noms = models.CharField(max_length=100)
    contact = models.CharField(max_length=50)
    avatar = models.ImageField(null=True, blank=True, upload_to="img/avatars/", default="img/avatars/default-user-img.png")

    class Meta():
        ordering = ['user', 'contact']

    def __str__(self):
        return f"Propriétaire - User: {self.noms} - Contact: {self.contact}"

    def statuLogeique(self):
        return f"Propriétaire"
    
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
    

class ImagesMaison(models.Model):
    maison = models.ForeignKey(House, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(null=True, blank=True, upload_to="img/maisons/")

    def __str__(self):
        return f"Maison: {self.maison} - Image: {self.image}"

