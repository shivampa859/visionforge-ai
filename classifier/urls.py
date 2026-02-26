from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),          # homepage
    path('predict/', views.index, name='index'),     # classifier page
]