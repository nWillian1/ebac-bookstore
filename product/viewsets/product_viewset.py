from rest_framework.viewsets import ModelViewSet # importando o ModelViewSet para criar uma viewset que fornece ações padrão para modelos Django

from product.models import Product # importando o modelo Product para usar na viewset
from product.serializers.product_serializer import ProductSerializer # importando o serializer ProductSerializer para usar na viewset

class ProductViewSet(ModelViewSet): # definindo a classe ProductViewSet que herda de ModelViewSet
    serializer_class = ProductSerializer # definindo o serializer_class para usar o ProductSerializer

    def get_queryset(self): # definindo o método get_queryset para retornar o queryset de produtos
        return Product.objects.all() # retornando todos os objetos do modelo Product