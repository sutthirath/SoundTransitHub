from django.urls import path
from . import views

urlpatterns = [
 path('', views.index, name='index'),
 path('signup/', views.signup, name='signup'),
 path('account/', views.account, name='account'),
 path('main/', views.main, name='main'),
 path('logout/', views.logout_view, name='logout'),
]