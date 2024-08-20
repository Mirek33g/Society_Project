from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.user_list),
    path('user/<int:pk>/', views.user_detail),
    path('address/', views.address_list),
    path('address/<int:pk>/', views.address_detail),
    path('post/', views.post_list),
    path('post/<int:pk>/', views.post_detail),
]
