from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from home.models import User, user_exists
from django.template import RequestContext, loader

# Create your views here.
def index(request):
    if request.method == "POST":
        if user_exists(request.POST['email']):
            return render("home.html")
        else:
           User(email=request.POST['email']).save()
        return render("home.html")
    else:
        return redirect('landing')


# Create your views here.
def landing(request):
    template = loader.get_template('landing.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))