from django.forms import model_to_dict
from django.shortcuts import render

# Create your views here.
from rest_framework import generics, viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from women.models import Women, Category
from women.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from women.serializers import WomenSerializer


class WomenAPIListPagination(PageNumberPagination):
    # по умолчанию
    page_size = 3
    # регулятор получения записей
    page_size_query_param = 'page_size'
    # Не более 10000.
    # Применяется только page_size_query_param
    max_page_size = 10000


# для наглядности разбили на классы для просмотра работы permission
class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    # должна быть коллекция или список
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = WomenAPIListPagination


class WomenAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    # permission_classes = (IsOwnerOrReadOnly,)
    permission_classes = (IsAuthenticated,)
    # предоставляет доступ только тем пользователям которые получают доступ по токенам
    # authentication_classes = (TokenAuthentication,)


class WomenAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAdminOrReadOnly,)

# # то же самое что и с параметром viewsets.ModelViewSet, только без возможности удалить
# class WomenViewSet(mixins.CreateModelMixin,
#                    mixins.RetrieveModelMixin,
#                    mixins.UpdateModelMixin,
#                    mixins.ListModelMixin,
#                    GenericViewSet):
#     # ссылает на список записей возращаемый клиенту
#     # queryset = Women.objects.all()
#     # сериализатор, который будет применять к queryset
#     serializer_class = WomenSerializer
#
#     # переопределение метода
#     def get_queryset(self):
#         pk = self.kwargs.get('pk')
#
#         if not pk:
#             # вывод первых 3 записей
#             return Women.objects.all()[:3]
#
#         return Women.objects.filter(pk=pk)
#
#     # создание своего машрута
#     # detail=True возращается одна запись
#     # имя машрута берётся на основе имени метода
#     # @action(methods=['get'], detail=True)
#     # def category(self, requests):
#     #     cats = Category.objects.all()
#     #     return Response({'cats': [c.name for c in cats]})
#
#     # http://127.0.0.1:8000/api/v1/women/1/category/
#     @action(methods=['get'], detail=True)
#     def category(self, requests, pk=None):
#         cats = Category.objects.get(pk=pk)
#         return Response({'cats': cats.name})

# # только для чтения
# class WomenViewSet(viewsets.ReadOnlyModelViewSet):
#     # ссылает на список записей возращаемый клиенту
#     queryset = Women.objects.all()
#     # сериализатор, который будет применять к queryset
#     serializer_class = WomenSerializer

# # убрали дублирования кода:
# # queryset = Women.objects.all()
# # serializer_class = WomenSerializer
# class WomenViewSet(viewsets.ModelViewSet):
#     # ссылает на список записей возращаемый клиенту
#     queryset = Women.objects.all()
#     # сериализатор, который будет применять к queryset
#     serializer_class = WomenSerializer

# # упрощённый вариант записи
# # реализует два метода GET и POST
# class WomenAPIList(generics.ListCreateAPIView):
#     # ссылает на список записей возращаемый клиенту
#     queryset = Women.objects.all()
#     # сериализатор, который будет применять к queryset
#     serializer_class = WomenSerializer
#
# # UpdateAPIView  позволяет выполнять 2 запроса put и patch
# class WomenAPIUpdate(generics.UpdateAPIView):
#     # ссылает на список записей возращаемый клиенту
#     # вернёт одну запись
#
#     # является ленивым запросом
#     # выполняются, когда требуются определённые данные, а жадные сразу
#     # класс UpdateAPIView сам обрабатывает запрос queryset и вернёт одну запись
#     queryset = Women.objects.all()
#     # сериализатор, который будет применять к queryset
#     serializer_class = WomenSerializer
#
# # UpdateAPIView  позволяет выполнять 2 запроса put и patch
# class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     # ссылает на список записей возращаемый клиенту
#     # вернёт одну запись
#
#     # является ленивым запросом
#     # выполняются, когда требуются определённые данные, а жадные сразу
#     # класс UpdateAPIView сам обрабатывает запрос queryset и вернёт одну запись
#     queryset = Women.objects.all()
#     # сериализатор, который будет применять к queryset
#     serializer_class = WomenSerializer

# усложнённый вид записи
# # APIView - стоит во главе иерархии всех классов представления Django Rest Framework
# # ListAPIView наследуется от APIView
# class WomenAPIView(APIView):
#     def get(self, request):
#         w = Women.objects.all()
#         # many=True - сериализатор должен обрабатывать список записей
#         return Response({'posts': WomenSerializer(w, many=True).data})
#
#     def post(self, request):
#         serializer = WomenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         # post_new = Women.objects.create(
#         #     title=request.data['title'],
#         #     content=request.data['content'],
#         #     cat_id=request.data['cat_id']
#         # )
#         # вместо post_new
#         serializer.save()
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': 'Method PUT not allowed'})
#
#         try:
#             instance = Women.objects.get(pk=pk)
#         except:
#             return Response({'error': 'Object does not exists'})
#
#         # сам определяет какой метод использовать (create или update). Смотрит по параметрам (data, instance)
#         # instance - запись, которую будем менять
#         serializer = WomenSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         # метод save() вызовет метод update, т.к. код создавали сериализатор были указаны 2 параметра
#         serializer.save()
#         return Response({'post': serializer.data})
#
#     def delete(self, request, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': 'Method DELETE not allowed'})
#
#         try:
#             instance = Women.objects.get(pk=pk)
#             instance.delete()
#         except:
#             return Response({'error': 'Object does not exists'})
#
#         return Response({'post': 'delete post ' + str(pk)})
# ДО
# def get(self, request):
#     lst = Women.objects.all().values()
#     return Response({'posts': list(lst)})
#
# def post(self, request):
#     post_new = Women.objects.create(
#         title=request.data['title'],
#         content=request.data['content'],
#         cat_id=request.data['cat_id']
#     )
#     # model_to_dict - преобразовывает модель django в словарь
#     return Response({'post': model_to_dict(post_new)})

# # представление
# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
