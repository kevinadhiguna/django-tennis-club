from django.urls import path
from . import views

app_name = 'members'

urlpatterns = [
  path('members/', views.members, name='members'),
]
