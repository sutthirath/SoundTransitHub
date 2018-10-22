from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('details/', views.details_view, name='details'),
    path('account/', views.account, name='account'),
    path('transit/main/', views.main, name='main'),
    path('transit/<int:transit_id>', views.reviews, name='reviews'),
    path('transit/create/', views.TransitCreate.as_view(), name='transit_create'),
    path('transit/<int:pk>/update/', views.TransitUpdate.as_view(), name='transit_update'),
    path('transit/<int:pk>/delete/', views.TransitDelete.as_view(), name='transit_delete'),
    path('logout/', views.logout_view, name='logout'),
]
