from rest_framework import viewsets
from rest_framework import generics
from . import serializers
from . import models
from rest_framework.response import Response

class Newletter(generics.CreateAPIView):
    queryset = models.Newletter.objects.all()
    serializer_class = serializers.NewletterSerializer

class ReseauViewset(viewsets.ModelViewSet):
    queryset = models.Reseau.objects.all()
    serializer_class = serializers.ReseauSerializer

class Contact(generics.CreateAPIView):
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactSerializer


class SiteinfoViewset(viewsets.ModelViewSet):
    queryset = models.Siteinfo.objects.all()
    serializer_class = serializers.SiteinfoSerializer

class AboutViewset(viewsets.ModelViewSet):
    queryset = models.About.objects.all()
    serializer_class = serializers.AboutSerializer

    

    