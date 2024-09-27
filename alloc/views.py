from django.shortcuts import render

def index(request):
    return render(request, 'alloc/index.html')
# Create your views here.
