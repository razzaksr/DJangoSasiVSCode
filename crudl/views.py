from django.shortcuts import render, redirect

from crudl.models import Candidates
from crudl.forms import CandidatesForm

candidates=[]
one=''

def initial(request):
    return render(request,'index.html')

def auth(request):
    user=request.POST['user']
    pas=request.POST['pass']
    if(user=='sasi' and pas=='kumarsalem'):
        one=user
        candidates=Candidates.objects.all()
        print(len(candidates))
        return render(request,"home.html",{"candidates":candidates,'who':one})
    else:
        return render(request,'index.html',{"info":"Login failed"})

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

def show(request):
    candidates=Candidates.objects.all()
    return render(request,"home.html",{"candidates":candidates,'who':one})

def edit(request,id):
    cand=Candidates.objects.get(id=id)
    return render(request,"edit.html",{"candidate":cand})

def update(request, id):  
    cand = Candidates.objects.get(id=id)  
    form = CandidatesForm(request.POST, instance = cand)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'candidate': cand})  

def remove(request,id):
    cand=Candidates.objects.get(id=id)
    cand.delete()
    return redirect("/show")

def find(request):
    return render(request,'find.html')

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
    return render(request,"home.html",{'candidates':candidates})


def printing(request):
    for x in candidates:
        print(x.name)
    return render(request,"home.html",{'candidates':candidates})
