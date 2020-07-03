from django.shortcuts import render
from blog import models as blog_models
from django.utils import timezone
from . import models
# Create your views here.
def index(request):
    siteinfo = models.Siteinfo.objects.filter(status=True).latest('date_update')
    about = models.About.objects.filter(status=True).latest('date_update')
    lieu = blog_models.Lieu.objects.filter(status=True)
    event = blog_models.Event.objects.filter(status=True)
    nky = event.filter(lieu__ville__icontains="new york")
    nextevent= event.filter(date_start__gt = str(timezone.now()))[:3]
    reseau_social = models.Reseau_social.objects.filter(status=True)
    partenaires = blog_models.Partner.objects.filter(status=True)
    

    datas = {
        "siteinfo":siteinfo,
        "about":about,
        "lieu":lieu,
        "reseau_social":reseau_social,
        "event":event[:11],
        "nextevent":nextevent,
        "nky":nky,
    }
    return render(request, 'pages/index.html', datas)

def contact(request):
    siteinfo = models.Siteinfo.objects.filter(status=True).latest('date_update')
    lieu = blog_models.Lieu.objects.filter(status=True)[:3]
    
    datas = {
        "lieu":lieu,
        "siteinfo":siteinfo,
        "marp": lieu[:1]
    }
    return render(request, 'pages/contact.html', datas)


def events(request):
    datas = {
        
    }
    return render(request, 'pages/events.html', datas)

