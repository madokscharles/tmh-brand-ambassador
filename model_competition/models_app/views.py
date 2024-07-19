# models_app/views.py

from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')