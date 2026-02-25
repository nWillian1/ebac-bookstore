from django.urls import path, include # imporando include para incluir as rotas do router
from rest_framework import routers # importando o viewset para criar as rotas automaticamente

from product import viewsets # importando o viewset para criar as rotas automaticamente

router = routers.SimpleRouter() # criando o router
router.register(r"product", viewsets.ProductViewSet, basename="product") # registrando o viewset no router
router.register(r"category", viewsets.CategoryViewSet, basename="category") # registrando o viewset no router

urlpatterns = [ # definindo as rotas para o app product
    path("", include(router.urls)), # incluindo as rotas do router
]
