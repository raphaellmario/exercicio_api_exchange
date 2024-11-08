from django.urls import path
from . import views

urlpatterns = [
    path('exchangerate_api/', views.exchangerate_api, name='exchangerate_api'),
    path('show/', views.show, name='exchangerate_api'),
]