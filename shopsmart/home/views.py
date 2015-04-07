from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from home.models import User, user_exists
from django.template import RequestContext, loader
from home.custom_shortcuts import render_with_no_context, render_with_context

# list of mobile User Agents
mobile_uas = [
    'w3c ','acs-','alav','alca','amoi','audi','avan','benq','bird','blac',
    'blaz','brew','cell','cldc','cmd-','dang','doco','eric','hipt','inno',
    'ipaq','java','jigs','kddi','keji','leno','lg-c','lg-d','lg-g','lge-',
    'maui','maxo','midp','mits','mmef','mobi','mot-','moto','mwbp','nec-',
    'newt','noki','oper','palm','pana','pant','phil','play','port','prox',
    'qwap','sage','sams','sany','sch-','sec-','send','seri','sgh-','shar',
    'sie-','siem','smal','smar','sony','sph-','symb','t-mo','teli','tim-',
    'tosh','tsm-','upg1','upsi','vk-v','voda','wap-','wapa','wapi','wapp',
    'wapr','webc','winw','winw','xda','xda-'
]

mobile_ua_hints = ['SymbianOS', 'Opera Mini', 'iPhone']


def mobile(request):
    mobile_browser = False
    ua = request.META['HTTP_USER_AGENT'].lower()[0:4]

    if ua in mobile_uas:
        mobile_browser = True
    else:
        for hint in mobile_ua_hints:
            if request.META['HTTP_USER_AGENT'].find(hint) > 0:
                mobile_browser = True

    return mobile_browser


def landing(request):
    if mobile(request):
        return render_with_no_context(request, 'landing_m.html')
    else:
        return render_with_no_context(request, 'landing.html')


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

