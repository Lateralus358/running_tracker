from django.shortcuts import render

# Create your views here.
def track_list(request):
    return render(request, 'tracker/track_list.html', {})