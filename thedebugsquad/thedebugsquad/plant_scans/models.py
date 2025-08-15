from django.db import models
from django.utils import timezone

class PlantScan(models.Model):
    """Model for storing plant scan information"""
    SCAN_STATUS_CHOICES = [
        ('pending', 'Pending Analysis'),
        ('completed', 'Analysis Completed'),
        ('failed', 'Analysis Failed'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='plant_scans/')
    upload_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, choices=SCAN_STATUS_CHOICES, default='pending')
    
    def __str__(self):
        return self.title

class DiagnosisResult(models.Model):
    """Model for storing diagnosis results"""
    plant_scan = models.OneToOneField(PlantScan, on_delete=models.CASCADE, related_name='diagnosis')
    disease_name = models.CharField(max_length=200, blank=True, null=True)
    confidence_score = models.FloatField(default=0.0)
    diagnosis_date = models.DateTimeField(default=timezone.now)
    additional_notes = models.TextField(blank=True, null=True)
    recommendations = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"Diagnosis for {self.plant_scan.title}"

class Subscription(models.Model):
    """Model for storing newsletter subscriptions"""
    email = models.EmailField(unique=True)
    subscribed_date = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.email 