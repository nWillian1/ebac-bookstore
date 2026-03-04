from rest_framework import (
    serializers,
)  # importando o módulo de serializers do Django Rest Framework

from product.models.product import (  # importando o modelo Product do aplicativo product
    Category,
    Product,
)
from product.serializers.category_serializer import (
    CategorySerializer,
)  # importando o serializer CategorySerializer do aplicativo product


class ProductSerializer(
    serializers.ModelSerializer
):  # criando um serializer para o modelo Product, que é uma subclasse de ModelSerializer
    category = CategorySerializer(
        required=True, many=True
    )  # definindo um campo de categoria, que é uma lista de categorias.
    categories_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), write_only=True, many=True
    )  # definindo um campo de IDs de categorias, que é uma lista de IDs de categorias. Este campo é write-only, ou seja, só pode ser usado para criar ou atualizar um produto, e não será incluído na representação do produto.

    class Meta:  # definindo a classe Meta para o serializer, que é usada para configurar o comportamento do serializer.
        model = Product  # definindo o modelo que o serializer irá usar, que é o modelo Product.
        fields = [
            "id",  # definindo o campo de ID, que é um campo de inteiro.
            "title",  # definindo o campo de título, que é um campo de texto.
            "description",  # definindo o campo de descrição, que é um campo de texto.
            "price",  # definindo o campo de preço, que é um campo decimal.
            "active",  # definindo o campo de ativo, que é um campo booleano.
            "category",  # definindo o campo de categoria, que é uma lista de categorias.
            "categories_id",  # definindo o campo de IDs de categorias, que é uma lista de IDs de categorias.
        ]

    def create(
        self, validated_data
    ):  # definindo um método para criar um produto a partir dos dados validados.
        category_data = validated_data.pop(
            "categories_id"
        )  # extraindo os dados das categorias do dicionário de dados validados.
        validated_data.pop(
            "category", None
        )  # removendo o campo de categoria do dicionário de dados validados, caso ele exista, para evitar conflitos com o campo de IDs de categorias.
        product = Product.objects.create(
            **validated_data
        )  # criando um novo produto com os dados validados.

        for category in category_data:  # iterando sobre a lista de IDs de categorias.
            product.category.add(
                category
            )  # adicionando cada categoria ao produto usando o método add() do campo de categoria do modelo Product.

        return product  # retornando o produto criado.
