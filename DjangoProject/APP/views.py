from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
def hello(request):
    return HttpResponse("<h1>Hello, Soneyo!</h1>")

def var(request):
    name="Harsh"
    return HttpResponse(f"The name is "+name)
    # return HttpResponse("The name is {name}")

def sum(request):
    number1=10
    number2=20
    return HttpResponse(f"The sum is {number1 + number2}")

def func(request):
    items={
        "a":"about a",
        "b":"about b",
        "c":"about c",
    }
    context="<h1>Menu Items</h1>"
    for item, description in items.items():
        context += f"<li>{item}: {description}</li>"
    return HttpResponse(context)

def getval(request, a, b):
    return HttpResponse(f"The values are {a} and {b}")

def query(request):
    name=request.GET.get("name")
    roll=request.GET.get("roll")
    return HttpResponse(f"The username = {name} and roll number = {roll}")
    #https://127.0.0.1:8000/query/?name=John&roll=12204666

def jsonVal(request):
    data = {"name": "Harsh","roll": 12204666,"course": "Btech CSE"}
    return JsonResponse(data)

# def getapi(request):
#     import requests
#     response = requests.get("https://api.sampleapis.com/coffee/hot")
#     data=response.json()
#     return JsonResponse(data, safe=False)

from django.shortcuts import render

def include_page(request):
    return render(request, "inc.html")

def first(request):
    context={'name':'Harsh'}
    return render(request,"APP/child.html",context)


def home(request):
    context = {
        "Username": "Harsh",
        "password": "12345",
        "otp": "9876",
        "mylist": ["Apple", "Banana", "Cherry"]
    }
    return render(request, "APP/child.html", context)
def include_page(request):
    return render(request, "APP/inc.html")


def image(request):
    return render(request, "APP/image.html")

# Q1) Given a variable user_name passed to the template write the template code to display "Hello,<user_name>!" only if the variable exists

# Q2) Given a list students with each student having a name, write a template snippet that displays a numbered list (1. Name) of all students names.
def student_list(request):
    students = ["Alice", "Bob", "Charlie", "David"]
    context = {"students": students}
    return render(request, "APP/student.html", context)

# Q3) You have list of books and each book has a is_available attribute write a snippet that lists the titles of only the available books

