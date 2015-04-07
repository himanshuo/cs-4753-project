from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from home.models import User, user_exists


# Create your views here.
def index(request):
    if request.method == "POST":
        if user_exists(request.POST['email']):
            return render_to_response("home.html")
        else:
           User(email=request.POST['email']).save()
        return render_to_response("home.html")
    else:
        return redirect('landing')


# Create your views here.
def landing(request):
    return render_to_response("landing.html")