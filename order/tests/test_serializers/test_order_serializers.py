from django.test import TestCase # importa a classe TestCase do módulo django.test para criar testes unitários para a aplicação Django.
from product.factories import ProductFactory # importa a fábrica de produto do módulo product.factories para criar instâncias de produto para os testes.
from order.factories import OrderFactory # importa a fábrica de pedido do módulo order.factories para criar instâncias de pedido para os testes.
from order.serializers import OrderSerializer # importa o serializer de pedido do módulo order.serializers para testar a serialização dos dados do pedido.

class TestOrderSerializer(TestCase): # define a classe de teste para o serializer de pedido, que herda da classe TestCase do Django.
    def setUp(self): # define o método setUp, que é executado antes de cada teste para configurar o ambiente de teste.
        self.product_1 = ProductFactory(price=100) # cria uma instância de produto usando a fábrica de produto, com o preço 100 para testar a criação do produto.
        self.product_2 = ProductFactory(price=250) # cria uma instância de produto usando a fábrica de produto, com o preço 250 para testar a criação do produto.
        self.order = OrderFactory() # cria uma instância de pedido usando a fábrica de pedido para testar a criação do pedido.
        
        self.order.product.add(self.product_1, self.product_2) # adiciona os produtos criados ao pedido usando o método add() do campo de produto do pedido.
        
        self.serializer = OrderSerializer(self.order) # cria uma instância do serializer de pedido, passando o pedido criado como argumento para testar a serialização dos dados do pedido.

    def test_order_serializer_total_calculation(self): # define o método de teste para verificar se o cálculo do total do pedido está correto após a serialização dos dados do pedido.
        data = self.serializer.data # obtém os dados serializados do pedido usando a propriedade data do serializer.
        
        self.assertEqual(data["total"], 350) # verifica se o campo "total" do JSON é igual a 350 usando o método assertEqual() do TestCase, garantindo que o total do pedido seja calculado corretamente com base nos preços dos produtos adicionados ao pedido.
        
    def test_order_serializer_product_count(self): # define o método de teste para verificar se a contagem de produtos no pedido está correta após a serialização dos dados do pedido.
        data = self.serializer.data # obtém os dados serializados do pedido usando a propriedade data do serializer.
        self.assertEqual(len(data["product"]), 2)  # verifica se o campo "product" do JSON contém a quantidade correta de produtos, verificando se o comprimento da lista de produtos é igual a 2 usando o método assertEqual() do TestCase, garantindo que todos os produtos adicionados ao pedido estejam presentes na serialização dos dados do pedido.