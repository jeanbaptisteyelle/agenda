from django.urls import path, include
from . import views
from . import apiviews
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('reseau', apiviews.ReseauViewset, basename='reseau')
router.register('siteinfo', apiviews.SiteinfoViewset, basename='siteinfo')
router.register('about', apiviews.AboutViewset, basename='about')

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('newletter', views.newletter, name='newletter'),
    
    path('events', views.events, name='events'),

    # Routes DES API

    path("api/", include(router.urls)),

    path('api-contact', apiviews.Contact.as_view(), name='contact'),
    path('api-newletter', apiviews.Newletter.as_view(), name='newletter'),


]

