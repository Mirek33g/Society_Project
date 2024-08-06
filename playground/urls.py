from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.users),
    path('user/<int:pk>/', views.user_detail),
    path('address/', views.all_address),
    path('address/<int:pk>/', views.address_detail),
]
