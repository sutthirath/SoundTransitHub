from django.db import models

# Create your models here.
class Account(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    user = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name