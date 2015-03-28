from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from models import *
from random import randrange
import random
import string

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
    if(request.method == 'POST'):
        l=[chr(randrange(0,26)+97) for i in range(10)]
        s=''.join(l)
        content = Content(
            links=request.POST['links'],
            title=request.POST['title'],
            abstract=request.POST['abstract']
        )
        content.date=timezone.now()
        content.article_id=s
        content.save()
        content.category.add(Category.objects.all()[0])
        return HttpResponseRedirect("/dashboard")
    else:
        return render(request, 'publish.html', {})

def dashboard(request):
    return render(request, 'dashboard.html', {})

