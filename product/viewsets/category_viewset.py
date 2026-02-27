from rest_framework.viewsets import ModelViewSet # importando o ModelViewSet para criar uma viewset que fornece ações padrão para modelos Django

from product.models import Category # importando o modelo Product para usar na viewset
from product.serializers.category_serializer import CategorySerializer # importando o serializer ProductSerializer para usar na viewset

class CategoryViewSet(ModelViewSet): # definindo a classe ProductViewSet que herda de ModelViewSet
    serializer_class = CategorySerializer # definindo o serializer_class para usar o ProductSerializer

    def get_queryset(self): # definindo o método get_queryset para retornar o queryset de produtos
        return Category.objects.all().order_by("id") # retornando todos os objetos do modelo Product