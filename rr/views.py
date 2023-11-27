from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def samson(request):
    return render(request,'samson.html')

def buttler(request):
    return HttpResponse('<h1>best strikers in cricket</h1>')