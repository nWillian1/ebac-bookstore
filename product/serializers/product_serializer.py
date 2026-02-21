from rest_framework import serializers # importando o módulo de serializers do Django Rest Framework

from product.models.product import Product # importando o modelo Product do aplicativo product
from product.serializers.category_serializer import CategorySerializer # importando o serializer CategorySerializer do aplicativo product

class ProductSerializer(serializers.ModelSerializer): # criando um serializer para o modelo Product, que é uma subclasse de ModelSerializer
    category = CategorySerializer(required=True, many=True) # definindo um campo de categoria, que é uma lista de categorias.

    class Meta: # definindo a classe Meta para o serializer, que é usada para configurar o comportamento do serializer.
        model = Product # definindo o modelo que o serializer irá usar, que é o modelo Product.
        fields = [ # definindo os campos que o serializer irá usar, que são o campo de título, descrição, preço, ativo e categoria.
            "title", # definindo o campo de título, que é um campo de texto.
            "description", # definindo o campo de descrição, que é um campo de texto.
            "price", # definindo o campo de preço, que é um campo decimal.
            "active", # definindo o campo de ativo, que é um campo booleano.
            "category", # definindo o campo de categoria, que é uma lista de categorias.
        ]
