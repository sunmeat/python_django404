from django.urls import path
from . import views

urlpatterns = [
    path('', views.branches_list, name='branches_list'),
    path('London/', views.london, name='london'), 
    path('Paris/', views.paris, name='paris'),
]