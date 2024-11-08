from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import requests


def exchangerate_api(request):
    a = ""
    return JsonResponse({'text':'Myfirst route'})

def show(request):
    key = "96563e0d2ed6d8c09d768788"
    url = "https://v6.exchangerate-api.com/v6/"+key+"/latest/USD"
    headers = {"Content-Type": "application/json"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return JsonResponse(response.json())
    else:
        print(f"Failed to retrieve data: {response.status_code}")