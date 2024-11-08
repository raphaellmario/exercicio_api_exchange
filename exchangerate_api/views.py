from django.http import HttpResponse
from django.shortcuts import render

def exchangerate_api(request):
    return HttpResponse("My first Route")
