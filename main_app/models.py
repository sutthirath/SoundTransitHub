from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=2)
    zipcode = models.IntegerField()

    def __str__(self):
        return self.user