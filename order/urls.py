from django.urls import (  # importando as funções path e include para definir as rotas da aplicação
    include,
    path,
)
from rest_framework import (
    routers,
)  # importando o DefaultRouter para criar rotas automaticamente

from order import viewsets  # importando as viewsets do aplicativo order

router = (
    routers.SimpleRouter()
)  # criando uma instância do SimpleRouter para registrar as rotas da viewset
router.register(
    r"order", viewsets.OrderViewSet, basename="order"
)  # registrando a viewset OrderViewSet com a rota 'orders'

urlpatterns = (
    [  # definindo as rotas da aplicação, incluindo as rotas geradas pelo router
        path(
            "", include(router.urls)
        ),  # incluindo as rotas geradas pelo router na URL principal do aplicativo
    ]
)
