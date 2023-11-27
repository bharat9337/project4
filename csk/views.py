from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def msd(request):
    return render (request,'msd.html')
def faf(request):
    return HttpResponse('<h1>best fielder</h1>')