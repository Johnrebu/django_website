from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homepage(request):
    msg="<h1>This is my Homepage of the Application</h1>"
    return HttpResponse(msg)

def home(request):
    msg="""<html>
    <head>
    <title>Welcome|Homepage</title>
    </head>
    <body>
    <h1>This is the homepage of the Application</h1>
    <h2><a href="/login">click here</a> to login Application</h2>
    <h2><a href="/register">click Here<a/> to Register Application</h2>
    <h2><a href="/payment">click Here<a/> to payment Application</h2>
    </body>
    </html>"""
    return HttpResponse(msg)

def register(request):
    msg="""<html>
    <head>
    <title>Welcome|Register page</title>
    </head>
    <body>
    <h1>This is the register page of the Application</h1>
    </body>
    </html>"""
    return HttpResponse(msg)

def login(request):
    msg="""<html>
    <head>
    <title>Welcome|LoginPage</title>
    </head>
    <body>
    <h1>This is the LoginPage of the Application</h1>
    </body>
    </html>"""
    return HttpResponse(msg)

def payment(request):
    return HttpResponse("""<html>
    <head>
    <title>Welcome|PaymentPage</title>
    </head>
    <body>
    <h1>This is the Payment page of the Application</h1>
    </body>
    </html>""")


def home(request):
    d={"name":"Manoj","age":"27"}
    return render(request,r"firstapp\homepage.html",d)












