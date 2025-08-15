from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import PlantScan, DiagnosisResult, Subscription
from .forms import PlantScanForm
import json

def upload_scan(request):
    if request.method == 'POST':
        form = PlantScanForm(request.POST, request.FILES)
        if form.is_valid():
            plant_scan = form.save()
            # Here we would normally call a function to analyze the plant image
            # For now, we'll just create a dummy diagnosis result
            DiagnosisResult.objects.create(
                plant_scan=plant_scan,
                disease_name="Sample Disease",
                confidence_score=0.85,
                additional_notes="This is a sample diagnosis result.",
                recommendations="Water the plant regularly and ensure it gets enough sunlight."
            )
            plant_scan.status = 'completed'
            plant_scan.save()
            return redirect('scan_detail', scan_id=plant_scan.id)
    else:
        form = PlantScanForm()
    
    return render(request, 'plant_scans/upload_scan.html', {'form': form})

def scan_history(request):
    scans = PlantScan.objects.all().order_by('-upload_date')
    return render(request, 'plant_scans/scan_history.html', {'scans': scans})

def scan_detail(request, scan_id):
    scan = get_object_or_404(PlantScan, id=scan_id)
    try:
        diagnosis = scan.diagnosis
    except DiagnosisResult.DoesNotExist:
        diagnosis = None
    
    return render(request, 'plant_scans/scan_detail.html', {
        'scan': scan,
        'diagnosis': diagnosis
    })

@csrf_exempt
@require_POST
def subscribe(request):
    try:
        data = json.loads(request.body)
        email = data.get('email')
        
        if not email:
            return JsonResponse({'success': False, 'message': 'Email is required'}, status=400)
        
        # Check if email already exists
        if Subscription.objects.filter(email=email).exists():
            return JsonResponse({'success': True, 'message': 'You are already subscribed'})
        
        # Create new subscription
        Subscription.objects.create(email=email)
        return JsonResponse({'success': True, 'message': 'Successfully subscribed'})
    
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)}, status=500) 