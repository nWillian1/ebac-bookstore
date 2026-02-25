import json # importando o módulo json para trabalhar com dados em formato JSON.
from rest_framework.test import APITestCase, APIClient # importando as classes APITestCase e APIClient do módulo rest_framework.test para criar testes de API.
from rest_framework.views import status # importando a classe status do módulo rest_framework.views para usar os códigos de status HTTP nas asserções dos testes.

from django.urls import reverse # importando a função reverse do módulo django.urls para gerar URLs a partir dos nomes das rotas definidas no arquivo urls.py.

from product.factories import ProductFactory, CategoryFactory # importando as fábricas de produtos e categorias do módulo product.factories para criar instâncias de produtos e categorias para os testes.
from order.factories import UserFactory # importando a fábrica de usuários do módulo order.factories para criar instâncias de usuários para os testes.
from product.models import Product # importando o modelo de produto do módulo product.models para acessar os dados dos produtos criados nos testes.

class TestProductViewSet(APITestCase): # definindo a classe de teste para o viewset de produtos, que herda da classe APITestCase do Django REST Framework.
    client = APIClient() # criando uma instância do cliente de API para fazer requisições HTTP nos testes.

    def setUp(self): # definindo o método de configuração para os testes, que é executado antes de cada teste.
        self.user = UserFactory() # criando um usuário usando a fábrica de usuários para associar aos produtos.

        self.product = ProductFactory(
            title="pro controller",
            price=500.00,
        )

    def test_get_all_products(self): # definindo o método de teste para obter todos os produtos.
        response = self.client.get(
            reverse("product-list")
        ) # fazendo uma requisição GET para a URL do endpoint de listagem de produtos usando a função reverse para gerar a URL a partir do nome da rota.

        self.assertEqual(response.status_code, status.HTTP_200_OK) # verificando se o status code da resposta é 200 OK.

        product_data = json.loads(response.content) # carregando o conteúdo da resposta como JSON e acessando o primeiro item da lista de produtos retornada.

        self.assertEqual(product_data[0]["title"], self.product.title) # verificando se o título do produto retornado é igual ao título do produto criado na configuração do teste.
        self.assertEqual(product_data[0]["price"], self.product.price) # verificando se o preço do produto retornado é igual ao preço do produto criado na configuração do teste.
        
        self.assertEqual(product_data[0]["title"], self.product.title)
        self.assertEqual(product_data[0]["price"], self.product.price)
        self.assertEqual(product_data[0]["active"], self.product.active) # verificando se o campo de ativo do produto retornado é igual ao campo de ativo do produto criado na configuração do teste.

    def test_create_product(self): # definindo o método de teste para criar um produto.
        category = CategoryFactory() # criando uma categoria usando a fábrica de categorias para associar ao produto.
        data = json.dumps({
            "title": "notebook",
            "price": 800.00,
            "categories_id": [category.id], # definindo o ID da categoria para associar ao produto.
            "category": [{"title": category.title, "slug": "slug-da-categoria"}] # definindo o ID da categoria para associar ao produto.
        }) # criando um dicionário de dados para criar o produto, convertendo-o para JSON usando a função json.dumps().

        response = self.client.post(
            reverse("product-list"),
            data=data,
            content_type="application/json"
        ) # fazendo uma requisição POST para a URL do endpoint de criação de produtos com os dados do produto em formato JSON.
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED) # verificando se o status code da resposta é 201 Created.

        created_product = Product.objects.get(title="notebook") # obtendo o produto criado a partir do banco de dados usando o ID retornado na resposta.

        self.assertEqual(created_product.title, "notebook") # verificando se o título do produto criado é igual ao título definido nos dados enviados na requisição.
        self.assertEqual(created_product.price, 800.00) # verificando se o preço do produto criado é igual ao preço definido nos dados enviados na requisição.