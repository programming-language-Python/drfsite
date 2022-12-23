"""drfsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import Route, SimpleRouter

from women.views import *
# from rest_framework import routers
#
#
# # from women.views import WomenAPIView
#
# # router служат для упрощения написания машрутов
# # создание своего router. Требуется иногда редко
# # лучше этот класс поместить в отдельный файл routers.py
# class MyCustomRouter(SimpleRouter):
#     """
#     A router for read-only APIs, which doesn't use trailing slashes.
#     """
#     routes = [
#         Route(
#             url=r'^{prefix}$',
#             mapping={'get': 'list'},
#             name='{basename}-list',
#             detail=False,
#             # дополнительные аргументы для коллекции kwargs
#             # которые передаются конкретному определению при срабатывании машрута
#             initkwargs={'suffix': 'List'}
#         ),
#         Route(
#             url=r'^{prefix}/{lookup}$',
#             mapping={'get': 'retrieve'},
#             name='{basename}-detail',
#             detail=True,
#             initkwargs={'suffix': 'Detail'}
#         )
#     ]
#
#
# # создали объект класса
# router = MyCustomRouter()
# # router = routers.SimpleRouter()
# # возращает список машрутов, которые присутствует в router
# # router = routers.DefaultRouter()
# # регистрация классов viewset
# # (префикс машрутов, класс viewSet)
# # имена формируются на основе имени модели
# # basename - изменяет имя. Если в views не задан queryset, то basename обязателен
# router.register(r'women', WomenViewSet, basename='women')
# # router.register(r'women', WomenViewSet)
# # print(router.urls)

urlpatterns = [
    path('admin/', admin.site.urls),

    # permission
    path('api/v1/women/', WomenAPIList.as_view()),
    path('api/v1/women/<int:pk>/', WomenAPIUpdate.as_view()),
    path('api/v1/womenDelete/<int:pk>', WomenAPIDestroy.as_view()),

    # # машрутизатор
    # # include(router.urls) - все машруты, которые находятся в коллекции urls
    # path('api/v1/', include(router.urls)),  # http://127.0.0.1:8000/api/v1/women/

    # # эти машрутизаторы были автоматизированы с помощью Routers
    # # {метод обработки запроса: метода который будет вызываться для обработки get запроса}
    # # list и update - стандартные методы
    # path('api/v1/womenList/', WomenViewSet.as_view({'get': 'list'})),
    # path('api/v1/womenList/<int:pk>/', WomenViewSet.as_view({'put': 'update'})),

    # # машрутизаторы короткой формы записи
    # path('api/v1/womenList/', WomenAPIList.as_view()),
    # # сам определяет какой из методов вызвать
    # path('api/v1/womenList/<int:pk>/', WomenAPIList.as_view()),
    # path('api/v1/womenList/<int:pk>/', WomenAPIUpdate.as_view()),
    # path('api/v1/womenDetail/<int:pk>/', WomenAPIDetailView.as_view()),

    # # машрутизаторы длинной формы записи
    # path('api/v1/womenList/', WomenAPIView.as_view()),
    # # сам определяет какой из методов вызвать
    # path('api/v1/womenList/<int:pk>/', WomenAPIView.as_view()),
]
