from django.db import models
from decimal import Decimal
import re
# Create your models here.


def user_exists(email):
    return User.objects.filter(email=email).exists()


class Coupon(models.Model):
    name=models.CharField(null=False, max_length=100)
    def calculate_price(self, original_price):
        """
        FOUR COUPONS ONLY:
            1) 50% off
            2) buy 1 get 1 free
            3) 1 dollar off
            4) 2 dollars off
        """
        if "buy 1 get 1 free" == self.name:
            return original_price
        elif "50% off" == self.name:
            return original_price*Decimal(.5)
        elif "1 dollar off" == self.name:
            return original_price-1
        else:
            return original_price-2


class Product(models.Model):
    title = models.CharField(null=False, max_length=100)
    description = models.CharField(null=False, max_length=1000)
    picture = models.CharField(null=False, max_length=500)
    rating = models.IntegerField(null=False, )
    price = models.DecimalField(null=False, max_digits=10, decimal_places=2)
    coupons = models.ManyToManyField(Coupon)



    def serialize(self):
        return {
            'title': self.title,
            'description':self.description,
            'picture': 'http://localhost:8000/static/images/'+self.picture,
            'available_coupons':  [c.name for c in self.coupons.all()],
            'rating':self.rating,
            'price':str(self.price),
            'id':self.id
        }


class User(models.Model):
    email = models.EmailField(null=False, unique=True)
    products_seen = models.ManyToManyField(Product)
