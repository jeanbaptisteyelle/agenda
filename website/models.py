from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class About(models.Model):
    titre = models.CharField( max_length=255)
    description = models.TextField()
    image = models.ImageField( upload_to='images/about')

    date_add = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)
    class Meta:
        verbose_name = "about"
        verbose_name_plural = "abouts"

    def __str__(self):
        return self.titre

class Siteinfo(models.Model):
    slogan = models.CharField( max_length=255)
    logo_H = models.ImageField( upload_to='images/about')

    date_add = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)
    class Meta:
        verbose_name = "Siteinfo"
        verbose_name_plural = "Siteinfos"

    def __str__(self):
        return self.slogan

    
class Contact(models.Model):
    nom = models.CharField( max_length=255)
    email = models.CharField( max_length=255)    
    subject = models.TextField(null=True)
    message = models.TextField()

    date_add = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)
    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return self.email

class Reseau_social(models.Model):
    ICONE =[
        ('fa fa-pinterest','pinterest'),
        ('fa fa-linkedin','linkedin'),
        ('fa fa-instagram','instagram'),
        ('fa fa-facebook','facebook'),
        ('fa fa-twitter','twitter'),
    ]

    nom = models.CharField(max_length=255)
    lien = models.URLField()
    icone = models.CharField(choices=ICONE, max_length=255)
    

    date_add = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Reseau_social"
        verbose_name_plural = "Reseau_sociaux"

    def __str__(self):
        return self.nom

class Newletter(models.Model):
    nom = models.CharField(max_length=255)
    email = models.EmailField()
    
    date_add = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)
    class Meta:
        verbose_name = "Newletter"
        verbose_name_plural = "Newletters"

    def __str__(self):
        return self.email

    






    

