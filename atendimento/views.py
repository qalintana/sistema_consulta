from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.
def teste(request:HttpRequest):
  return render(request, 'base.html')

def teste2(request:HttpRequest):
  return render(request, "index.html")