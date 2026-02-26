from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.news, name='news'),
    path('management/', views.management, name='management'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    
    # URL для розділу "Філії" !!!
    path('branches/', include('branches.urls')),
]