from rest_framework import serializers # importando o módulo de serializers do Django Rest Framework

from product.models import Product # importando o modelo Product do aplicativo product
from product.serializers.product_serializer import ProductSerializer # importando o serializer ProductSerializer do aplicativo product
from order.models import Order # importando o modelo Order do aplicativo order

class OrderSerializer(serializers.ModelSerializer): # criando um serializer para o modelo Order, que é uma subclasse de ModelSerializer
    product = ProductSerializer(required=True, many=True) # definindo um campo de produtos, que é uma lista de produtos.
    total = serializers.SerializerMethodField() # definindo um campo total.

    def get_total(self, instance): # definindo um método para calcular o total do pedido.
        total = sum([product.price for product in instance.product.all()]) # calculando o total do pedido somando o preço de cada produto na lista de produtos do pedido.
        return total # retornando o total do pedido.

    class Meta: # definindo a classe Meta para o serializer, que é usada para configurar o comportamento do serializer.
        model = Order # definindo o modelo que o serializer irá usar, que é o modelo Product.
        fields = ["product", "total", "user"] # definindo os campos que o serializer irá usar, que são o campo de produtos e o campo de total.