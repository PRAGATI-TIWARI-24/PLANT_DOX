from django.contrib import admin
from .models import PlantScan, DiagnosisResult, Subscription

class DiagnosisResultInline(admin.StackedInline):
    model = DiagnosisResult
    extra = 0

@admin.register(PlantScan)
class PlantScanAdmin(admin.ModelAdmin):
    list_display = ('title', 'upload_date', 'status')
    list_filter = ('status', 'upload_date')
    search_fields = ('title', 'description')
    inlines = [DiagnosisResultInline]

@admin.register(DiagnosisResult)
class DiagnosisResultAdmin(admin.ModelAdmin):
    list_display = ('plant_scan', 'disease_name', 'confidence_score', 'diagnosis_date')
    list_filter = ('diagnosis_date',)
    search_fields = ('disease_name', 'additional_notes', 'recommendations')

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_date', 'is_active')
    list_filter = ('subscribed_date', 'is_active')
    search_fields = ('email',) 