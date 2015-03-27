from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from models import *

# Create your views here.
def home(request):
    if('id' in request.GET):
        try:
            id = request.GET['id']
            content = Content.objects.get(article_id=id)
        except:
            return HttpResponse("No article found with this id!")
        return render(request, 'details.html', {'content' : content})
    else:
        categories = Category.objects.all()
        contents = Content.objects.all().order_by('-date')
        previous = []
        upcoming = []
        for i in contents:
            if(timezone.now() > i.date):
                previous.append(i)
            else:
                upcoming.append(i)
        previous = previous[:5]
        upcoming = upcoming[:5]
        return render(request, 'index.html', {'categories' : categories, 'previous' : previous, 'upcoming' : upcoming })

def publish(request):
    return render(request, 'publish.html', {})

def dashboard(request):
    return render(request, 'dashboard.html', {})

