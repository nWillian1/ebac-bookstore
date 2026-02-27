from rest_framework.viewsets import ModelViewSet    # importando o ModelViewSet para criar uma viewset que fornece ações padrão para modelos Django
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication # importando as classes de autenticação para a viewset
from rest_framework.permissions import IsAuthenticated # importando as classes de permissão para a viewset e verificar se o usuário está autenticado

from product.models import Product # importando o modelo Product para usar na viewset
from product.serializers.product_serializer import ProductSerializer # importando o serializer ProductSerializer para usar na viewset

class ProductViewSet(ModelViewSet): # definindo a classe ProductViewSet que herda de ModelViewSet
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication] # define as classes de autenticação para a viewset 
    permission_classes = [IsAuthenticated] # define as classes de permissão para a viewset 
    serializer_class = ProductSerializer # define o serializer_class para usar o ProductSerializer

    def get_queryset(self): # definindo o método get_queryset para retornar o queryset de produtos
        return Product.objects.all().order_by("id") # retornando todos os objetos do modelo Product