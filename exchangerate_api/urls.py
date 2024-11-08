from django.urls import path
from . import views

urlpatterns = [
    path('exchangerate_api/', views.exchangerate_api, name='exchangerate_api'),
]