from django.contrib import admin
from .models import Account, Transit, Comment

# Register your models here.

admin.site.register(Account)
admin.site.register(Transit)
admin.site.register(Comment)
