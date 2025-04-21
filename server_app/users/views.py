from rest_framework import generics
from .models import User
from .serializers import UserSerializer


# Класс для чтения-записи
# представления коллекции экземпляров модели.
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Класс для чтения или обновления конечных точек
# для представления одного экземпляра модели
class UserRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
