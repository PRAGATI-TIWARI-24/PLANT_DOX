from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_scan, name='upload_scan'),
    path('history/', views.scan_history, name='scan_history'),
    path('detail/<int:scan_id>/', views.scan_detail, name='scan_detail'),
    path('subscribe/', views.subscribe, name='subscribe'),
] 