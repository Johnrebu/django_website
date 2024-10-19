from django.contrib import messages
from django.shortcuts import render

# Create your views here.
def samplealert(request):
    return render(request,"alertapp/messageapp.html")

def success(request):
    messages.success(request,"This is a success message")
    return render(request,"alertapp/messageapp.html")

def error(request):
    messages.error(request,"This is a error message")
    return render(request,"alertapp/messageapp.html")

def warning(request):
    messages.warning(request,"This is a warning message")
    return render(request,"alertapp/messageapp.html")

def info(request):
    messages.info(request,"This is a info message")
    return render(request,"alertapp/messageapp.html")