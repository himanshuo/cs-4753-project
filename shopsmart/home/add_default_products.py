__author__ = 'himanshu'
from models import Product

"""
class Product(models.Model):
    title = models.CharField(null=False, max_length=100)
    description = models.CharField(null=False)
    picture = models.ImageField(null=False)
    rating = models.IntegerField(null=False)
    price = models.DecimalField(null=False)
    coupons = models.ManyToManyField(Coupon)
"""


Product(
    title='Slingshot',
    description='To keep your frienemies away when you need to.',
    picture='slingshot.jpg',
    rating=4,
    price=14.99,
).save()

Product(
    title='Beanie Baby',
    description='A timeless toy for all ages and genders',
    picture='beanie.jpg',
    rating=5,
    price=24.49,
).save()


Product(
    title='White T-shirt',
    description='Your typical white tee - very comfortable!',
    picture='tshirt.jpg',
    rating=3,
    price=3.99,
).save()

Product(
    title='Red Solo Cup',
    description='Better than the ones you’ll find at your typical frat party! (100)',
    picture='cup.jpg',
    rating=4,
    price=7.99,
).save()

Product(
    title='Portable Apparatus for Sitting',
    description='Patent protected',
    picture='chair.jpg',
    rating=1,
    price=12.69,
).save()


Product(
    title='Cannon',
    description='More effective than a slingshot',
    picture='cannon.jpg',
    rating=5,
    price=299.99,
).save()



Product(
    title='Haribo Sugarless Gummy Bears',
    description='5 pounds of diarrhea!',
    picture='haribo.jpg',
    rating=5,
    price=12.99,
).save()

