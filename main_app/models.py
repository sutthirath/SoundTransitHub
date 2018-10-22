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
        return reverse('main')

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transit = models.ForeignKey(Transit, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('reviews', kwargs={'comment_id': self.id})