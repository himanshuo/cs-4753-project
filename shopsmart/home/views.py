from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from home.models import User, user_exists, Product, Coupon
from django.template import RequestContext, loader
from home.custom_shortcuts import render_with_no_context, render_with_context

# code used from mobiForge by ronan
#####################################
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
######################################


def landing(request):
    if mobile(request):
        return render_with_no_context(request, 'landing_m.html')
    else:
        return render_with_no_context(request, 'landing.html')


def products(request):

    products = Product.objects.all()
    print(products)

    for p in products:
        p.rating=range(p.rating)
        p.picture = 'http://localhost:8000/static/images/'+p.picture
        p.available_coupons = p.coupons.all()
        print(str(p.available_coupons))
    print("below is product list:")
    print(products)
    return render_with_context(request, 'products.html', {
        'products' : products
    })


def email(request):

    u = User.objects.get(email=request.session['email'])
    if request.method == "POST":
        u.email = request.POST['email']
        request.session["email"] = request.POST['email']
        u.save()

    email_id = u.email
    return render_with_context(request, 'email.html', {'email': email_id})


# Create your views here.
def index(request):
    if request.method == "POST":
        new_user=False
        if user_exists(request.POST['email']):
            print(request.POST['email']+' exists already')
            if not request.session.get('email'):
                request.session["email"] = request.POST['email']

        else:
            new_user |= True # FALSE OR TRUE = TRUE. make new_user true.
            u = User(email=request.POST['email'])
            u.save()

            if not request.session.get('email'):
                request.session["email"] = request.POST['email']

        u = User.objects.get(email=request.session['email'])
        products = u.products_seen.all()

        for p in products:
            p.rating = range(p.rating)
            p.picture = 'http://localhost:8000/static/images/'+p.picture
            p.available_coupons = p.coupons.all()
            print(str(p.available_coupons))
        return render_with_context(request, 'home.html', {
            'products' : products,
            'new_user': new_user,
            'user_email': request.POST['email']
        })

    else:
        return redirect('landing')


def price_check(request):
    product_id = request.GET["product_id"]
    print(product_id)
    the_product = Product.objects.get(pk=product_id)
    return render_with_context(request, 'price_check.html', {'product': the_product})


def user_is_logged_in():
    pass


def add_stuff(request):

    c1 = Coupon(name="50% off")
    c1.save()
    c2 = Coupon(name="buy 1 get 1 free")
    c2.save()
    c3 = Coupon(name="1 dollar off")
    c3.save()
    c4 = Coupon(name="2 dollars off")
    c4.save()

    Product(
        title='Slingshot',
        description='To keep your frienemies away when you need to.',
        picture='slingshot.jpg',
        rating=4,
        price=14.99,
    ).save()

    p=Product(
        title='Beanie Baby',
        description='A timeless toy for all ages and genders',
        picture='beanie.jpg',
        rating=5,
        price=24.49,
    )
    p.save()
    p.coupons.add(c2)
    p.save()


    Product(
        title='White T-shirt',
        description='Your typical white tee - very comfortable!',
        picture='tshirt.jpg',
        rating=3,
        price=3.99,
    ).save()

    p= Product(
        title='Red Solo Cup',
        description='Better than the ones you’ll find at your typical frat party! (100)',
        picture='cup.jpg',
        rating=4,
        price=7.99,
    )
    p.save()
    p.coupons.add(c4)
    p.save()

    p=Product(
        title='Portable Apparatus for Sitting',
        description='Patent protected',
        picture='chair.jpg',
        rating=1,
        price=12.69,
    )
    p.save()
    p.coupons.add(c1)
    p.save()


    Product(
        title='Cannon',
        description='More effective than a slingshot',
        picture='cannon.jpg',
        rating=5,
        price=299.99,
    ).save()



    p=Product(
        title='Haribo Sugarless Gummy Bears',
        description='5 pounds of diarrhea!',
        picture='haribo.jpg',
        rating=5,
        price=12.99,
    )
    p.save()
    p.coupons.add(c2)
    p.save()

    return HttpResponse("done.")