from django.shortcuts import render
from blog import models as blog_models
from . import models
# Create your views here.
def index(request):
    siteinfo = models.Siteinfo.objects.filter(status=True).latest('date_update')
    about = models.About.objects.filter(status=True).latest('date_update')
    lieu = blog_models.Lieu.objects.filter(status=True)
    event = blog_models.Event.objects.filter(status=True)[:11]
    reseau_social = models.Reseau_social.objects.filter(status=True)
    partenaires = blog_models.Partner.objects.filter(status=True)

    datas = {
        "siteinfo":siteinfo,
        "about":about,
        "lieu":lieu,
        "reseau_social":reseau_social,
        "event":event,
    }
    return render(request, 'pages/index.html', datas)

def contact(request):
    datas = {
        
    }
    return render(request, 'pages/contact.html', datas)


def events(request):
    datas = {
        
    }
    return render(request, 'pages/events.html', datas)

