from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from .models import EmployeeDetails
from .forms import EmployeeForm, FormClass


# Create your views here.

def employeeDetails(request):
    employees = EmployeeDetails.objects.all()
    return render(request, "modelapp/AllDatas.html",context={"employees":employees})


def createemployee(request):
    if(request.method=="POST"):
        if (request.POST.get("employeeid")and request.POST.get("username")
                and request.POST.get("password")and request.POST.get("designation")
                and request.POST.get("phonenumber")):
            register = EmployeeDetails()
            register.empid=request.POST.get("employeeid")
            register.username=request.POST.get("username")
            register.password= request.POST.get("password")
            register.designation= request.POST.get("designation")
            register.phno= request.POST.get("phonenumber")
            register.save()
            return HttpResponse("<h2>SuccessFully stored in the Database Table<a href='model/get'>Click Here</a> to redirect to HomePage</h2>")
        else:
            return HttpResponse("some Fields details are missing")

    forms=EmployeeForm()
    return render(request, "modelapp/EmployeeForm.html",context={"forms":forms})

def showDate(request):
    day = datetime.now().day
    month = datetime.now().month

    def chris():
        if (day == 14 & month == 12):
            return "christmas"
        else:
            return "No christmas"
    result = chris()
    print(result)

    return render(request,'ModelApp/showDate.html',context={"day":day,"month":month})

def sampleform(request):
    form=FormClass()
    return render(request,"modelapp/FormFields.html",context={"form":form})

def searchitems(request):
    srch=request.GET.get("search")
    if srch:
        employees=EmployeeDetails.objects.filter(Q(username__icontains=srch) | Q(empid__icontains=srch) | Q(phno__icontains=srch))
        emp_count=employees.count()
    else:
        employees=EmployeeDetails.objects.all()
        emp_count = employees.count()
    return render(request,"modelapp/AllDatas.html",context={"employees":employees,"count":emp_count})













