from django.urls import path
from .views import UserListCreateView, UserRetrieveUpdateView

urlpatterns = [
    path('users/', UserListCreateView.as_view()),
    path('users/<int:pk>/', UserRetrieveUpdateView.as_view()),
]
