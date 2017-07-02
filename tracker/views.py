from django.shortcuts import render
from django.utils import timezone
from .models import Tracker

# Create your views here.
def track_list(request):
    tracking_data = Tracker.objects.filter(run_date__lte=timezone.now()).order_by('-run_date')
    return render(request, 'tracker/track_list.html', {'tracking_data' : tracking_data})

def tracker_dashboard(request):
    return render(request, 'tracker/tracker_dash.html', {})