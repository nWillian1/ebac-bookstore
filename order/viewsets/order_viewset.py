from rest_framework.authentication import (  # importando as classes de autenticação para a viewset
    BasicAuthentication,
    SessionAuthentication,
    TokenAuthentication,
)
from rest_framework.permissions import (
    IsAuthenticated,
)  # importando as classes de permissão para a viewset e verificar se o usuário está autenticado
from rest_framework.viewsets import (
    ModelViewSet,
)  # importando o ModelViewSet para criar uma viewset que fornece ações padrão para modelos Django

from order.models import (
    Order,
)  # importando o modelo Order para usar na viewset
from order.serializers import (
    OrderSerializer,
)  # importando o serializer OrderSerializer para usar na viewset


class OrderViewSet(ModelViewSet):  # criando a viewset para o modelo Order
    authentication_classes = [
        SessionAuthentication,
        BasicAuthentication,
        TokenAuthentication,
    ]  # define as classes de autenticação para a viewset
    permission_classes = [
        IsAuthenticated
    ]  # define as classes de permissão para a viewset
    serializer_class = OrderSerializer  # definindo o serializer a ser usado para serializar os objetos Order
    queryset = Order.objects.all().order_by(
        "id"
    )  # definindo o queryset para a viewset, que retorna todos os objetos Order
