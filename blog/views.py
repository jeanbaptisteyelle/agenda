from django.shortcuts import render

# Create your views here.
def events_news(request):
    datas = {
        
    }
    return render(request, 'pages/events-news.html', datas)

def single_event(request):
    datas = {
        
    }
    return render(request, 'pages/single-event.html', datas)
