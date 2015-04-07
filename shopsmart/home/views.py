from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from home.models import User, user_exists, Product, Coupon
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