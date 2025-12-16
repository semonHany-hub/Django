from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome_view(request):
    return HttpResponse("Welcome to Digithup!")

def training_tracks(request):
    return HttpResponse("Available tracks for training->  Flutter,  Django")