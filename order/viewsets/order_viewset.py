from rest_framework.viewsets import ModelViewSet # importando o ModelViewSet para criar uma viewset que fornece ações padrão para modelos Django

from order.models import Order # importando o modelo Order para usar na viewset
from order.serializers import OrderSerializer # importando o serializer OrderSerializer para usar na viewset

class OrderViewSet(ModelViewSet): # criando a viewset para o modelo Order
    serializer_class = OrderSerializer # definindo o serializer a ser usado para serializar os objetos Order
    queryset = Order.objects.all() # definindo o queryset para a viewset, que retorna todos os objetos Order