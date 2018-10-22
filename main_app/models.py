from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=2)
    zipcode = models.IntegerField()

    def __str__(self):
        return self.user.username

class Transit(models.Model):
    branch = models.CharField(max_length=20)
    transit_type = models.CharField(max_length=20)
    route = models.CharField(max_length=50)
    time = models.CharField(max_length=20)

    def __str__(self):
        return self.route

    def get_absolute_url(self):
        return reverse('detail', kwargs={'transit_id': self.id})
