from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.apps import users


# Create your views here.
def index(request):
    print('index being called.')
    return render_to_response("home.html")


# Create your views here.
def landing(request):
    return render_to_response("landing.html")