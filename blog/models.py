from django.db import models

# Create your models here.
class Categorie(models.Model):
    nom = models.CharField(max_length=255)

    date_add = models.DateField(auto_now=True)
    date_update = models.DateField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Categorie"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.nom

class Tag(models.Model):
    nom = models.CharField(max_length=255)

    date_add = models.DateField(auto_now=True)
    date_update = models.DateField(auto_now=True)
    status = models.BooleanField(default=True)
    

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.nom

class Lieu(models.Model):
    ville = models.CharField(max_length=255)
    description = models.TextField() 
    marp_url = models.TextField()
    telephone = models.IntegerField()
    adresse = models.CharField(max_length=255)
    email = models.URLField()

    date_add = models.DateField(auto_now=True)
    date_update = models.DateField(auto_now=True)
    status = models.BooleanField(default=True)
    class Meta:
        verbose_name = "Lieu"
        verbose_name_plural = "Lieux"

    def __str__(self):
        return self.ville

class Event(models.Model):
    titre = models.CharField(max_length=255)
    lieu =  models.ForeignKey(Lieu, on_delete=models.CASCADE, related_name='lieu_Event')
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    prix = models.FloatField()
    description = models.TextField()
    organisateurs = models.TextField()
    tags = models.ManyToManyField(Tag)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='categorie_Event')
    image = models.ImageField(upload_to='image/Event')

    date_add = models.DateField(auto_now=True)
    date_update = models.DateField(auto_now=True)
    status = models.BooleanField(default=True)
    

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"

    def __str__(self):
        return self.titre
    
class New(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_new')
    image = models.ImageField(upload_to='image/new')

    date_add = models.DateField(auto_now=True)
    date_update = models.DateField(auto_now=True)
    status = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "New"
        verbose_name_plural = "News"

    def __str__(self):
        return self.titre

class Partner(models.Model):
    nom = models.CharField( max_length=255)
    image = models.ImageField(upload_to="immage/Partner")
    lien = models.URLField()

    date_add = models.DateField(auto_now=True)
    date_update = models.DateField(auto_now=True)
    status = models.BooleanField(default=True)
    
    

    class Meta:
        verbose_name = "Partner"
        verbose_name_plural = "Partners"

    def __str__(self):
        return self.nom

   

   





