from django.test import TestCase # importa a classe TestCase do módulo django.test para criar testes unitários para a aplicação Django.
from product.factories import ProductFactory # importa a fábrica de produto do módulo product.factories para criar instâncias de produto para os testes.

class TestProductModel(TestCase): # define a classe de teste para o modelo de produto, que herda da classe TestCase do Django.
    def setUp(self): # define o método setUp, que é executado antes de cada teste para configurar o ambiente de teste.
        self.product = ProductFactory(title="Teclado Mecânico") # cria uma instância de produto usando a fábrica de produto, com o título "Teclado Mecânico" para testar a criação do produto.

    def test_product_creation(self): # define o método de teste para verificar se o produto é criado corretamente.
        """Verifica se o produto é criado com o título correto""" # define a docstring para o método de teste, explicando o que ele faz.
        self.assertEqual(self.product.title, "Teclado Mecânico") # verifica se o campo "title" do produto é igual a "Teclado Mecânico" usando o método assertEqual() do TestCase.
        self.assertTrue(self.product.active)  # verifica se o campo "active" do produto é True usando o método assertTrue() do TestCase, garantindo que o produto esteja ativo por padrão.