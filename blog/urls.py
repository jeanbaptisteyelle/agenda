from django.urls import path
from . import views
urlpatterns = [
    path('single-event', views.single_event, name='single-event'),
    path('events-news', views.events_news, name='events-news'),
    path('single_event/<slug>',views.single_event,name="single_event")
]