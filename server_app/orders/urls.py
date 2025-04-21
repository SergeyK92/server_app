from django.urls import path
from .views import OrderListCreateView, OrderRetrieveUpdateView

urlpatterns = [
    path('orders/', OrderListCreateView.as_view()),
    path('orders/<int:pk>/', OrderRetrieveUpdateView.as_view()),
]
