from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html', {})

def details(request):
    return render(request, 'abstract.html', {})

def test(request):
    return render(request, 'test.html', {})

def details1(request):
    return render(request, 'index2.html', {})

def publish(request):
    return render(request, 'index3.html', {})

def dashboard(request):
    return render(request, 'index4.html', {})