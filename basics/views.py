from django.shortcuts import render
from django.http import HttpResponse
from . import models
from basics.models import Candidates
from basics.forms import CandidatesForm

# Create your views here.

def hai(request):
    return HttpResponse('<h1>Zealous Tech Corp</h1>')

def temp(request):
    return render(request,'index.html')

def initial(request):
    return render(request,'index.html')

def auth(request):
    user=request.POST['user']
    pas=request.POST['pass']
    if(user=='sasi' and pas=='kumarsalem'):
        return render(request,'home.html',{'who':user})
    else:
        return render(request,'index.html',{"info":"Login failed"})


def getEnroll(request):
    return render(request,'enroll.html')

def setEnroll(request):
    if request.method=="POST":
        object=CandidatesForm(request.POST)
        if object.is_valid():
            try:
                print('object before save',object)
                object.save()
                print('object saved',object)
                return redirect("/")
            except:pass
    else:
        object=CandidatesForm()
        print("NEw form called")
    return render(request,"enroll.html",{"obj":object})

    