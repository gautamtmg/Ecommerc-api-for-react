from django.urls import path 
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('users/login', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/register', views.registerUser, name='register'),
    path('users/profile/update/', views.updateUserProfile, name ='profile-update'),
  
    path('products/', views.getProducts, name="products"),
    path('products/<str:pk>/', views.getProduct, name= "product"),


    path('users/profile/', views.getUserProfile, name="user-profile"),
    path('users/', views.getUsers, name="users"),

    # order
    path('orders/add/', views.addOrderItems, name='add-order'),
    path('orders/myorders/', views.getMyOrders, name='my-orders'),
    path('orders/<str:pk>/', views.getOrderById, name='user-order'),
    path('orders/<str:pk>/pay/', views.updateOrderToPaid, name='pay'),

]
