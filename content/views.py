from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html', {})

def details(request):
    return render(request, 'details/content.html', {})