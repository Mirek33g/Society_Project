from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.users),
    path('user/<int:tk>/', views.user_detail),
]
