from rest_framework import (
    serializers,
)  # importando o módulo de serializers do Django Rest Framework

from order.models import Order  # importando o modelo Order do aplicativo order
from product.models import (
    Product,
)  # importando o modelo Product do aplicativo product
from product.serializers.product_serializer import (
    ProductSerializer,
)  # importando o serializer ProductSerializer do aplicativo product


class OrderSerializer(
    serializers.ModelSerializer
):  # criando um serializer para o modelo Order, que é uma subclasse de ModelSerializer
    product = ProductSerializer(
        required=True, many=True
    )  # definindo um campo de produtos, que é uma lista de produtos.
    products_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), write_only=True, many=True
    )  # definindo um campo de IDs de produtos, que é uma lista de IDs de produtos. Este campo é write-only, ou seja, só pode ser usado para criar ou atualizar um pedido, e não será incluído na representação do pedido.
    total = serializers.SerializerMethodField()  # definindo um campo total.

    def get_total(
        self, instance
    ):  # definindo um método para calcular o total do pedido.
        total = sum(
            [product.price for product in instance.product.all()]
        )  # calculando o total do pedido somando o preço de cada produto na lista de produtos do pedido.
        return total  # retornando o total do pedido.

    class Meta:  # definindo a classe Meta para o serializer, que é usada para configurar o comportamento do serializer.
        model = Order  # definindo o modelo que o serializer irá usar, que é o modelo Product.
        fields = [
            "product",
            "total",
            "user",
            "products_id",
        ]  # definindo os campos que o serializer irá usar, que são o campo de produtos e o campo de total.
        extra_kwargs = {
            "product": {"required": False}
        }  # definindo que o campo de produtos não é obrigatório, ou seja, pode ser omitido na criação de um pedido.

    def create(
        self, validated_data
    ):  # definindo um método para criar um pedido a partir dos dados validados.
        product_data = validated_data.pop(
            "products_id"
        )  # extraindo os dados dos produtos do dicionário de dados validados.
        user_data = validated_data.pop(
            "user"
        )  # extraindo os dados do usuário do dicionário de dados validados.
        order = Order.objects.create(
            user=user_data
        )  # criando um novo pedido com os dados do usuário.

        for product in product_data:  # iterando sobre a lista de IDs de produtos.
            order.product.add(
                product
            )  # adicionando cada produto ao pedido usando o método add() do campo de produtos do modelo Order.

        return order  # retornando o pedido criado.
