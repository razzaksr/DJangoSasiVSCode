from django.http import response
from django.shortcuts import render

# Create your views here.

def First(request):
    return render(request,"hai.html",{"hai":"Zealous"});