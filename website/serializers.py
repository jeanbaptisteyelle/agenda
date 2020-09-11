from rest_framework import serializers
from . import models

class NewletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Newletter
        fields = '__all__'

class ReseauSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Reseau
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contact
        fields = '__all__'

class SiteinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Siteinfo
        fields = '__all__'

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.About
        fields = '__all__'