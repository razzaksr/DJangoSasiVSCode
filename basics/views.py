from django.shortcuts import render
from django.http import HttpResponse

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
    a=int(request.POST['regno'])
    b=request.POST['name']
    c=request.POST['gender']
    d=request.POST['dept']
    e=int(request.POST['batch'])
    f=int(request.POST['contact'])
    g=request.POST['email']
    h=request.POST['add']
    i=float(request.POST['cgpa'])
    j=float(request.POST['hsc'])
    k=float(request.POST['diploma'])
    l=float(request.POST['sslc'])
    m=request.POST['interest']
    n=request.POST['skills']

    