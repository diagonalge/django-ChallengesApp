from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def jan(request):
    return HttpResponse("Eat no meat for the entire month!")

def feb(request):
    return HttpResponse("Walk for 30 minutes everyday.")