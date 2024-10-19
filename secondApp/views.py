import datetime

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def secondapp(request):
    return HttpResponse("This is a secondapp")


def ipltable(request):
    d=datetime.datetime.now()
    return render(request,"secondapp/ipltable.html",context={"name":"Vivo","date":d})

def pricelist(request):
    return render(request,"secondapp/Pricelist.html")

def total(request):
    mobiles=int(request.GET["mobiles"])
    laptop = int(request.GET["laptop"])
    keyboard = int(request.GET["keyboard"])
    pendrive = int(request.GET["pendrive"])
    mouse = int(request.GET["mouse"])
    tv=mobiles+laptop+keyboard+pendrive+mouse
    return render(request,"secondapp/TotalPrice.html",context={"values":tv})






