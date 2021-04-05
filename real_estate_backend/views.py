from django.shortcuts import render
from .models import Properties


# homepage view
def home(request):
    properties = Properties.objects.all()
    return render(
        request, 
        'index.html', 
        {'properties':properties})