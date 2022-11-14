from django.urls import path
from backend import views


urlpatterns = [
    path('orders',views.orderApi)
]