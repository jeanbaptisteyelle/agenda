from django.shortcuts import render
from website import models as website_models
from django.utils import timezone
from . import models
# Create your views here.
def events_news(request):
    siteinfo = website_models.Siteinfo.objects.filter(status=True).latest('date_update')
    new = models.New.objects.filter(status=True)[:3]
    event = models.Event.objects.filter(status=True).latest('date_update')

    datas = {
        "siteinfo":siteinfo,
        "new":new,
        "event":event,
    }
    return render(request, 'pages/events-news.html', datas)

def single_event(request):
    siteinfo = website_models.Siteinfo.objects.filter(status=True).latest('date_update')

    datas = {
        "siteinfo":siteinfo,
    
    }
    return render(request, 'pages/single-event.html', datas)
