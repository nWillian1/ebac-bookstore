import json # importando o módulo json para trabalhar com dados em formato JSON.
from rest_framework.test import APITestCase, APIClient # importando as classes APITestCase e APIClient do módulo rest_framework.test para criar testes de API.
from rest_framework.views import status # importando a classe status do módulo rest_framework.views para usar os códigos de status HTTP nas asserções dos testes.

from django.urls import reverse # importando a função reverse do módulo django.urls para gerar URLs a partir dos nomes das rotas definidas no arquivo urls.py.

from product.factories import CategoryFactory # importando as fábricas de produtos e categorias do módulo product.factories para criar instâncias de produtos e categorias para os testes.
from product.models import Category# importando o modelo de produto do módulo product.models para acessar os dados dos produtos criados nos testes.

class CategoryViewSet(APITestCase): # definindo a classe de teste para o viewset de produtos, que herda da classe APITestCase do Django REST Framework.
    client = APIClient() # criando uma instância do cliente de API para fazer requisições HTTP nos testes.

    def setUp(self): # definindo o método de configuração para os testes, que é executado antes de cada teste.
        self.category = CategoryFactory(title="books") # criando uma categoria usando a fábrica de categorias para associar aos produtos.

    def test_get_all_category(self): # definindo o método de teste para obter todas as categorias.
        response = self.client.get(
            reverse("category-list")
        ) # fazendo uma requisição GET para a URL do endpoint de listagem de categorias usando a função reverse para gerar a URL a partir do nome da rota.

        self.assertEqual(response.status_code, status.HTTP_200_OK) # verificando se o status code da resposta é 200 OK.
        category_data = json.loads(response.content) # carregando o conteúdo da resposta como JSON e acessando o primeiro item da lista de produtos retornada.

        self.assertEqual(category_data[0]["title"], self.category.title) # verificando se o título da categoria retornado é igual ao título da categoria criada na configuração do teste.

    def test_create_category(self): # definindo o método de teste para criar uma categoria.
        data = json.dumps({
            "title": "tecnology",
}) # criando um dicionário de dados para criar a categoria, convertendo-o para JSON usando a função json.dumps().

        response = self.client.post(
            reverse("category-list"),
            data=data,
            content_type="application/json"
        ) # fazendo uma requisição POST para a URL do endpoint de criação de categorias com os dados da categoria em formato JSON.

        self.assertEqual(response.status_code, status.HTTP_201_CREATED) # verificando se o status code da resposta é 201 Created.

        created_category = Category.objects.get(title="tecnology") # obtendo a categoria criada a partir do banco de dados usando o título retornado na resposta.

        self.assertEqual(created_category.title, "tecnology") # verificando se o título da categoria criada é igual ao título definido nos dados enviados na requisição.
