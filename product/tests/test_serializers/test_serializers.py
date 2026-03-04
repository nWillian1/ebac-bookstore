from django.test import (
    TestCase,
)  # importa a classe TestCase do módulo django.test para criar testes unitários para a aplicação Django.

from product.factories import (  # importa as fábricas de categoria e produto do módulo product.factories para criar instâncias de categoria e produto para os testes.
    CategoryFactory,
    ProductFactory,
)
from product.serializers.product_serializer import (
    ProductSerializer,
)  # importa o serializer de produto do módulo product.serializers.product_serializer para testar a serialização dos dados do produto.


class TestProductSerializer(
    TestCase
):  # define a classe de teste para o serializer de produto, que herda da classe TestCase do Django.
    def setUp(
        self,
    ):  # define o método setUp, que é executado antes de cada teste para configurar o ambiente de teste.
        self.category = CategoryFactory(
            title="eletronicos"
        )  # cria uma instância de categoria usando a fábrica de categoria, com o título "eletronicos".
        self.product = ProductFactory(
            title="mouse", price=100
        )  # cria uma instância de produto usando a fábrica de produto, com o título "mouse" e preço 100.
        self.product.category.add(
            self.category
        )  # adiciona a categoria criada ao produto usando o método add() do campo de categoria do produto.
        self.serializer = ProductSerializer(
            self.product
        )  # cria uma instância do serializer de produto, passando o produto criado como argumento para testar a serialização dos dados do produto.

    def test_product_serializer_fields(
        self,
    ):  # define o método de teste para verificar se os campos do JSON estão corretos após a serialização do produto.
        """Verifica se os campos do JSON estão corretos"""  # define a docstring para o método de teste, explicando o que ele faz.
        data = (
            self.serializer.data
        )  # obtém os dados serializados do produto usando a propriedade data do serializer.
        self.assertEqual(
            data["title"], "mouse"
        )  # verifica se o campo "title" do JSON é igual a "mouse" usando o método assertEqual() do TestCase.
        self.assertEqual(
            data["price"], 100
        )  # verifica se o campo "price" do JSON é igual a 100 usando o método assertEqual() do TestCase.
        self.assertEqual(
            data["category"][0]["title"], "eletronicos"
        )  # verifica se o campo "category" do JSON contém a categoria correta, acessando o primeiro elemento da lista de categorias e verificando se o título é igual a "eletronicos".
