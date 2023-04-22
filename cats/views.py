from rest_framework import generics

from .models import Cat
from .serializers import CatSerializer


class CatList(generics.ListCreateAPIView):
    # возвращает всю коллекцию объектов (например, всех котиков)
    # или может создать новую запись в БД
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


class CatDetail(generics.RetrieveUpdateDestroyAPIView):
    # возвращает обновляет или удаляет объекты модели по одному
    queryset = Cat.objects.all()
    serializer_class = CatSerializer