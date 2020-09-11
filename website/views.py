from django.shortcuts import render, redirect

from blog import models as blog_models
from django.utils import timezone
from . import models
import datetime
now = datetime.datetime.now()
next_date = now + datetime.timedelta(days=40)
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def newletter(request):
       if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        try:
            validate_email(email)
            if  name is not None :
                newletter = models.Newletter(
                    nom = name, 
                    email = email

                )
                newletter.save()
                messages.success(request,"vos informations ont été enregistré")
            else:
                messages.error(request,"Veuillez entrer un nom")
             
        except:
            messages.error(request, "veuillez entrer un email correct")
        return redirect(request.META.get('HTTP_REFERER', '/'))
            
        

def index(request):      
    siteinfo = models.Siteinfo.objects.filter(status=True)[:1].get()
    print(siteinfo)
    about = models.About.objects.get(status=True)
    lieu = blog_models.Lieu.objects.filter(status=True)
    event = blog_models.Event.objects.filter(status=True)
    nky = event.filter(lieu__ville__icontains="new york")
    nextevent= event.filter(date_start__gt = str(timezone.now()))[:3]
    reseau = models.Reseau.objects.filter(status=True)
    partenaires = blog_models.Partner.objects.filter(status=True)

    datas = {
       
        "siteinfo":siteinfo,
        "about":about,
        "lieu":lieu,
        "reseau":reseau,
        "event":event[:11],
        "nextevent":nextevent,
        "nky":nky,
        "partenaires": partenaires,
    }
    return render(request, 'pages/index.html', datas)

def contact(request):
    siteinfo = models.Siteinfo.objects.filter(status=True).latest('date_update')
    lieu = blog_models.Lieu.objects.filter(status=True)
    reseau = models.Reseau.objects.filter(status=True)
    
    datas = {
        "lieu":lieu[:3],
        "siteinfo":siteinfo,
        "marp": lieu.last,
        "reseau":reseau,
    }
    return render(request, 'pages/contact.html', datas)

def events(request):
    event = blog_models.Event.objects.filter(status=True)[:6]
    upcoming = blog_models.Event.objects.filter(date_start__gt = next_date)[:3]
    reseau = models.Reseau.objects.filter(status=True)
    siteinfo = models.Siteinfo.objects.filter(status=True).latest('date_update')
    datas = {
        "reseau":reseau,
        "event":event,
        "siteinfo":siteinfo,
        "upcoming":upcoming,
    }
    return render(request, 'pages/events.html', datas)