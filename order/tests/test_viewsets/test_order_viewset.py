import json

from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase

from order.factories import OrderFactory, UserFactory
from order.models import Order
from product.factories import CategoryFactory, ProductFactory
from product.models import Product


class TestOrderViewSet(APITestCase):

    client = APIClient()

    def setUp(self):
        self.user = (
            UserFactory()
        )  # criando um usuário usando a fábrica de usuários para associar ao pedido.
        self.token = Token.objects.create(
            user=self.user
        )  # criando um token para autenticar o usuário no teste.
        self.token.save()  # salvando o token no banco de dados.

        self.category = CategoryFactory(
            title="technology"
        )  # Cria uma categoria usando a fábrica de categorias para associar aos produtos.
        self.product = ProductFactory(
            title="Smartphone", price=1000, category=[self.category]
        )  # Cria um produto usando a fábrica de produtos para associar ao pedido.
        self.order = OrderFactory(
            product=[self.product], user=self.user
        )  # Cria um pedido usando a fábrica de pedidos para testar a criação do pedido.

    def test_order(self):
        self.client.credentials(
            HTTP_AUTHORIZATION="Token " + self.token.key
        )  # Adicionando o token de autenticação ao cliente de API.
        response = self.client.get(
            reverse("order-list", kwargs={"version": "v1"})
        )  # Faz uma requisição GET para a URL do endpoint de listagem de pedidos.

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )  # Verifica se o status code da resposta é 200 OK.

        order_data = json.loads(
            response.content
        )  # Carrega o conteúdo da resposta como JSON.
        self.assertEqual(
            order_data["results"][0]["product"][0]["title"], self.product.title
        )  # Verifica se o título do produto no pedido é igual ao título do produto criado na configuração do teste.
        self.assertEqual(
            order_data["results"][0]["product"][0]["price"], self.product.price
        )  # Verifica se o preço do produto no pedido é igual ao preço do produto criado na configuração do teste.
        self.assertEqual(
            order_data["results"][0]["product"][0]["active"],
            self.product.active,
        )  # Verifica se o título do produto no pedido é igual ao título do produto criado na configuração do teste.
        self.assertEqual(
            order_data["results"][0]["product"][0]["category"][0]["title"],
            self.category.title,
        )  # Verifica se o título da categoria do produto no pedido é igual ao título da categoria criada na configuração do teste.

    def test_create_order(self):
        self.client.credentials(
            HTTP_AUTHORIZATION="Token " + self.token.key
        )  # Adicionando o token de autenticação ao cliente de API.
        user = (
            UserFactory()
        )  # Cria um usuário usando a fábrica de usuários para associar ao pedido.
        product = (
            ProductFactory()
        )  # Cria um produto usando a fábrica de produtos para associar ao pedido.
        data = json.dumps(
            {
                "products_id": [
                    product.id
                ],  # Define os IDs dos produtos para criar o pedido.
                "user": user.id,  # Define o ID do usuário para criar o pedido.
            }
        )

        response = self.client.post(  # Faz uma requisição POST para a URL do endpoint de criação de pedidos com os dados do pedido em formato JSON.
            reverse("order-list", kwargs={"version": "v1"}),
            data=data,
            content_type="application/json",
        )

        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )  # Verifica se o status code da resposta é 201 Created.

        created_order = Order.objects.get(
            user=user
        )  # Obtém o pedido criado a partir do banco de dados usando o ID retornado na resposta.
