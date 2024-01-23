from django.urls import path
from . import views

app_name = 'members'

urlpatterns = [
  path('', views.main, name='main'),
  path('members/', views.members, name='members'),
  path('members/detail/<slug:slug>/', views.details, name='details'),
  path('testing/', views.testing, name='testing'),
]
