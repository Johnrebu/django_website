from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm, CreateUserForm
from django.contrib.auth import authenticate,login ,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator
from django.core import serializers

# Create your views here.
@login_required(login_url="/crud/login")
def getemployee(request):
    employee=Employee.objects.all()
    p=Paginator(employee,5)
    page=request.GET.get('page')
    perpage=p.get_page(page)

    lower_limit=max(perpage.number-2,1) # 1-3 -2,1
    high_limit=min(perpage.number+2,perpage.paginator.num_pages) #7 10
    data=serializers.serialize('json',perpage)
    return HttpResponse(data,content_type="application/json")
    return render(request, "crudapp/getAllemployee.html",context={"employee":employee,"perpage":perpage,"range":range(lower_limit,high_limit+1)})

@login_required(login_url="/crud/login")
def createemployee(request):
    if request.method=="POST":
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            #return HttpResponse("<h2>Successfully Saved the data in Table<a href='/crud/get'>Click Here</a> to redirect to HomePage</h2>")
            return redirect('/crud/get')
        else:
            return HttpResponse("<h2>Fill all the details</h2>")
    form=EmployeeForm()
    return render(request,"crudapp/addemployee.html",context={"form":form})
@login_required(login_url="/crud/login")
def deleteuser(request,id):
    emp= Employee.objects.get(id=id)
    if request.method=="POST":
        emp.delete()
        return redirect("/crud/get")
    return render(request,"crudapp/deleteemployee.html",context={"name":emp.name})

@login_required(login_url="/crud/login")
def updateemployee(request,id):
    emp=Employee.objects.get(id=id)
    if request.method=="POST":
        form=EmployeeForm(request.POST,instance=emp)
        if form.is_valid():
            form.save()
            return redirect('/crud/get')
        else:
            return HttpResponse("<h2>Fill all the details</h2>")
    return render(request,"crudapp/updateemployee.html",context={"emp":emp})

def loginpage(request):
    page='login'
    if request.user.is_authenticated:
        return redirect("/crud/get")
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        try:
           user=User.objects.get(username=username)
        except:
            messages.error(request,"Username is not exist")
        user= authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("/crud/get")
        else:
            messages.error(request,"Username and password does not request")

    return render(request,"crudapp/login_register.html",context={'page':page})





def logoutuser(request):
    logout(request)
    return redirect("/crud/login")


def registeruser(request):
    form=CreateUserForm()
    if request.method=="POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/crud/login")
        else:
            messages.error(request,"Registration failed")
    return render(request,"crudapp/login_register.html",context={"form":form})



















