from django.urls import path
from dakuoblog import views

urlpatterns = [
    path('', views.home, name='home'),
]
