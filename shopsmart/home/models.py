from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField(null=False, unique=True)


def user_exists(self, email):
    return User.objects.filter(email=email).exists()