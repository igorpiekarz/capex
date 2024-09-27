from django.shortcuts import render

def index(request):
    return render(request, 'psr/index.html')
# Create your views here.
