from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'dakuoblog/base.html', {})

def about_owner(request):
    return render(request, 'dakuoblog/about.html', {})
