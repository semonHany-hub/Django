from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def greeting_message(request):
    return HttpResponse("Hello, semon hany...")

def birth_date(request):
    return HttpResponse("1/11/2004")