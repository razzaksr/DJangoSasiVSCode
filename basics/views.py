from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hai(request):
    return HttpResponse('<h1>Zealous Tech Corp</h1>')

def temp(request):
    return render(request,'index.html')