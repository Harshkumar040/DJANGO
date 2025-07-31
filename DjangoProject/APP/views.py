from django.shortcuts import render
from django.http import HttpResponse
def hello(request):
    return HttpResponse("<h1>Hello, Soneyo!</h1>")

def var(request):
    name="Harsh"
    return HttpResponse("The name is "+name)