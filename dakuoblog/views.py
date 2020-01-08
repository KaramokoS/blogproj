from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'dakuoblog/base.html', {})

def expo(request):
    return render(request, 'dakuoblog/expositions.html', {})
