from django.urls import path
from dakuoblog import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('exposition/', views.expo, name='expo')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
