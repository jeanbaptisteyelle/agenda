from django.shortcuts import render, get_object_or_404
from website import models as website_models
from django.utils import timezone
from . import models
import datetime
now = datetime.datetime.now()
next_date = now + datetime.timedelta(days=40)

# Create your views here.
def events_news(request):
    siteinfo = website_models.Siteinfo.objects.filter(status=True).latest('date_update')
    new = models.New.objects.filter(status=True)[:3]
    event = models.Event.objects.filter(status=True).latest('date_update')
    reseau = website_models.Reseau.objects.filter(status=True)
    datas = {
        "siteinfo":siteinfo,
        "new":new,
        "event":event,
        "reseau":reseau[:3],
        
       
    }
    return render(request, 'pages/events-news.html', datas)

def single_event(request,slug):
    new = models.New.objects.get(slug=slug)
    reseau = website_models.Reseau.objects.filter(status=True)
    siteinfo = website_models.Siteinfo.objects.filter(status=True).latest('date_update')
    event = models.Event.objects.filter(status=True).latest('date_update')
    single_new = get_object_or_404(models.New, slug=slug)
    upcoming = models.Event.objects.filter(date_start__gt = next_date)[:3]


    datas = {
        "reseau":reseau,
        "new":new,
        "siteinfo":siteinfo,
        "event":event,
        "single_new": single_new,
        "upcoming":upcoming,
    
    }
    return render(request, 'pages/single-event.html', datas)

