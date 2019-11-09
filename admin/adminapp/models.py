from django.db import models
from django_better_admin_arrayfield.models.fields import ArrayField
from django.contrib.postgres.fields import JSONField , IntegerRangeField ,DateTimeRangeField
from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField
# Create your models here.

class Categorie(models.Model):
    """Model definition for Categorie."""

    # TODO: Define fields here
    nom = models.CharField(max_length=245)
    description = models.TextField()
    image = FilerImageField(related_name='image_cat',on_delete=models.DO_NOTHING)
    status = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Categorie."""

        verbose_name = 'Categorie'
        verbose_name_plural = 'Categories'

    def __str__(self):
        """Unicode representation of Categorie."""
        return self.nom

class SousCategorie(models.Model):
    """Model definition for SousCategorie."""

    # TODO: Define fields here
    nom = models.CharField(max_length=245)
    image = FilerImageField(related_name='image_sous',on_delete=models.DO_NOTHING)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='categorie')
    status = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for SousCategorie."""

        verbose_name = 'SousCategorie'
        verbose_name_plural = 'SousCategories'

    def __str__(self):
        """Unicode representation of SousCategorie."""
        return self.nom


class Tag(models.Model):
    """Model definition for Tag."""

    # TODO: Define fields here
    nom = models.CharField(max_length=50)
    status = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_updt = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Tag."""

        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        """Unicode representation of Tag."""
        return self.nom

class Produit(models.Model):

    titre = models.CharField(max_length=255)
    description = models.TextField()
    taille = ArrayField(models.IntegerField(),size=10,null=True)
    famille = JSONField(null=True)
    prix = IntegerRangeField(range(1, 50),null=True)
    periode_promo = DateTimeRangeField()
    tag = models.ManyToManyField(Tag, related_name='tag')
    image = FilerImageField(related_name='image_produit',on_delete=models.DO_NOTHING)
    sous_cat = models.ForeignKey(SousCategorie, on_delete=models.CASCADE, related_name='sous_cat')
    status = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_updt = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'produit'
        verbose_name_plural = 'produits'
        
    def __str__(self):
        return self.titre
