from django.shortcuts import render
from django.http import HttpResponse
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