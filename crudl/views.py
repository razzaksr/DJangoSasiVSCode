from django.shortcuts import render, redirect
from datetime import *
from crudl.models import Candidates, Companies
from crudl.forms import CandidatesForm, CompaniesForm


# Create your views here.
def company(request):
    if request.method=="POST":
        print("Inside view as post request")
        object=CompaniesForm(request.POST)
        if object.is_valid():
            print("valid object")
            try:
                print('object before save',object)
                object.save()
                print('object saved',object)
                return redirect("/comshow")
            except:pass
    else:
        object=CompaniesForm()
        print("NEw form called")
    return render(request,"comenroll.html",{"obj":object})


one=''

temp=[]

def initial(request):
    return render(request,'index.html')

def auth(request):
    user=request.POST['user']
    pas=request.POST['pass']
    if(user=='sasi' and pas=='kumarsalem'):
        one=user
        return render(request,"home.html",{'who':one})
    else:
        return render(request,'index.html',{"info":"Login failed"})

def parent(request):
    return render(request,'home.html',{'who':one})
''' 
def auth(request):
    user=request.POST['user']
    pas=request.POST['pass']
    if(user=='sasi' and pas=='kumarsalem'):
        one=user
        candidates=Candidates.objects.all()
        print(len(candidates))

        temp.clear();
        for x in candidates:
            cand=Candidates.objects.get(id=x.id)
            temp.append(cand)
        
        
        return render(request,"home.html",{"candidates":candidates,'who':one})
    else:
        return render(request,'index.html',{"info":"Login failed"}) '''

# Create your views here.
def candidate(request):
    if request.method=="POST":
        print("Inside view as post request")
        object=CandidatesForm(request.POST)
        if object.is_valid():
            print("valid object")
            try:
                print('object before save',object)
                object.save()
                print('object saved',object)
                return redirect("/show")
            except:pass
    else:
        object=CandidatesForm()
        print("NEw form called")
    return render(request,"enroll.html",{"obj":object})

def comshow(request):
    print("comshow function invoked")
    companies=Companies.objects.all()

    temp.clear();
    for x in companies:
            comp=Companies.objects.get(id=x.id)
            temp.append(comp)

    return render(request,"comhome.html",{"companies":companies,'who':one})

def show(request):
    print("show function invoked")
    candidates=Candidates.objects.all()

    temp.clear();
    for x in candidates:
            cand=Candidates.objects.get(id=x.id)
            temp.append(cand)

    return render(request,"canhome.html",{"candidates":candidates,'who':one})

def edit(request,id):
    cand=Candidates.objects.get(id=id)
    return render(request,"edit.html",{"candidate":cand})

def editcom(request,id):
    com=Companies.objects.get(id=id)
    return render(request,"comedit.html",{"company":com})

def update(request, id):  
    cand = Candidates.objects.get(id=id)  
    form = CandidatesForm(request.POST, instance = cand)  
    if form.is_valid(): 
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'candidate': cand})  


def updatecom(request, id):  
    com = Companies.objects.get(id=id)  
    form = CompaniesForm(request.POST, instance = com)  
    if form.is_valid(): 
        form.save()  
        return redirect("/comshow")  
    return render(request, 'comedit.html', {'company': com})

def remove(request,id):
    cand=Candidates.objects.get(id=id)
    cand.delete()
    return redirect("/show")

def removecom(request,id):
    com=Companies.objects.get(id=id)
    com.delete()
    return redirect("/comshow")

def find(request):
    return render(request,'find.html')

def findcom(request):
    return render(request,'comfind.html')

def look(request):
    reg=request.POST['regno']
    sk=request.POST['skills']
    dp=request.POST['dept']
    st=request.POST['status']
    candidates = Candidates.objects.all()
    #reg=111
    if reg!="" and sk=="" and dp=="Select One" and st=="Select One":
        reg=int(reg)
        can=[]
        for x in candidates:
            if x.regno == reg:
                can.insert(0,x)
    elif reg=="" and sk!="" and dp=="Select One" and st=="Select One":
        can=[]
        for x in candidates:
            if sk in x.skills:
                can.append(x)
    candidates=can
    temp.clear();
    for x in candidates:
            cand=Candidates.objects.get(id=x.id)
            temp.append(cand)
    return render(request,"canhome.html",{'candidates':candidates})


def lookcom(request):
    org=request.POST['org']
    sk=request.POST['skills']
    dt=request.POST['date']
    ct=request.POST['count']
    companies = Companies.objects.all()
    #reg=111
    if org!="" and sk=="" and dt=="" and ct=="":
        com=[]
        for x in companies:
            if x.org == org:
                com.append(x)
    elif org=="" and sk!="" and dt=="" and ct=="":
        com=[]
        for x in companies:
            if sk in x.role:
                com.append(x)
    elif org=="" and sk=="" and dt!="" and ct=="":
        dt=date(dt)
        com=[]
        for x in companies:
            if dt in x.date:
                com.append(x)
    elif org=="" and sk=="" and dt=="" and ct!="":
        ct=int(ct)
        com=[]
        for x in companies:
            if ct <= x.taken:
                com.append(x)
    companies=com
    temp.clear();
    for x in companies:
            com=Companies.objects.get(id=x.id)
            temp.append(com)
    return render(request,"comhome.html",{'companies':companies})

def filter(request):
    companies=Companies.objects.all()
    temp.clear()
    for x in companies:
        if x.date> date.today():
            temp.append(x)
            print(x.org)
    return render(request,'comfilter.html',{'companies':temp})

def info(request):
    key=int(request.POST['org'])
    companies=Companies.objects.all()
    only=Companies.objects.get(id=key)
    temp.clear()
    for x in companies:
        if x.date> date.today():
            temp.append(x)
            print(x.org)
    return render(request,'comfilter.html',{'obj':only,'companies':temp})

def fildo(request,key):
    key=int(key)
    candidates = Candidates.objects.all()
    company = Companies.objects.get(id=key)
    temp.clear()
    for x in candidates:
        if company.role in x.skills:
            temp.append(x)
    return render(request,'filtered.html',{"obj":company,"candidates":temp})

def printing(request):
    for x in temp:
        print(x.name)

    
    
    return render(request,"canhome.html",{'candidates':temp})
