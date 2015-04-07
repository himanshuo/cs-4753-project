from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from home.models import User, user_exists
from django.template import RequestContext, loader
from home.custom_shortcuts import render_with_no_context, render_with_context

# Create your views here.
def index(request):
    if request.method == "POST":
        if user_exists(request.POST['email']):
            print(request.POST['email']+' exists already' )
            return render_with_no_context(request, 'home.html')
        else:
            print('new user')
            User(email=request.POST['email']).save()
        return render_with_no_context(request, 'home.html')
    else:
        return redirect('landing')


# Create your views here.
def landing(request):
    return render_with_no_context(request, 'landing.html')