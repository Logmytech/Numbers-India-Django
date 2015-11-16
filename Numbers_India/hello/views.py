from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def mobilenumbers(request):
    return render(request, 'mobilenumbers.html')

def pincodes(request):
    return render(request, 'pincodes.html')

def stdcodes(request):
    return render(request, 'stdcodes.html')

def vehiclenumbers(request):
    return render(request, 'vehicle.html')
