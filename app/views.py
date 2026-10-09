from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


data= open('D:\HTML J SPIDER\CSS\swiggy.html')
def pitambar(Request):
    try:
        content=data.read()
        return HttpResponse(content)
    except:
        return HttpResponse("Error ")
    