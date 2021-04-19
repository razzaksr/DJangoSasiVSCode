from django.shortcuts import render, redirect

from crudl.models import Candidates
from crudl.forms import CandidatesForm

can=''

def initial(request):
    return render(request,'index.html')

def auth(request):
    user=request.POST['user']
    pas=request.POST['pass']
    if(user=='sasi' and pas=='kumarsalem'):
        can=user
        candidates=Candidates.objects.all()
        return render(request,"home.html",{"candidates":candidates,'who':can})
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
    return render(request,"home.html",{"candidates":candidates,'who':can})

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