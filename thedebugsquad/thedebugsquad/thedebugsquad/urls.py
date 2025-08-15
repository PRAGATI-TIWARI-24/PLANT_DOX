"""
URL configuration for thedebugsquad project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from thedebugsquad import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about-us/', views.aboutUs),
    path('homepage', views.homepage),
    path('scan/', views.scan),
    path('scan2/', views.scan2),
    path('guide/', views.guide, name='guide'),
    path('userform/', views.userform),
    path('index/',views.index),
    path('calc/',views.calc),
    path('plant-scans/', include('plant_scans.urls')),
    path('', views.homepage, name='home'),
]

# Add media URL configuration for handling uploaded images
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
