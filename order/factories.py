import factory # importando o módulo de factory do Python, que é usado para criar objetos de teste de forma fácil e rápida.

from django.contrib.auth.models import User # importando o modelo User do Django, que é usado para criar objetos de teste de usuário.
from product.factories import ProductFactory # importando a fábrica ProductFactory do aplicativo product, que é usada para criar objetos de teste de produto.

from order.models import Order # importando o modelo Order do aplicativo order, que é usado para criar objetos de teste de pedido.

class UserFactory(factory.django.DjangoModelFactory): # criando uma fábrica para o modelo Order, que é uma subclasse de DjangoModelFactory
    email = factory.Faker("pystr") # definindo o campo de usuário, que é um campo de texto, usando o método Faker do factory para gerar um valor aleatório.
    username = factory.Faker("pystr") # definindo o campo de nome de usuário, que é um campo de texto, usando o método Faker do factory para gerar um valor aleatório.

    class Meta: # definindo a classe Meta para a fábrica, que é usada para configurar o comportamento da fábrica.
        model = User # definindo o modelo que a fábrica irá usar, que é o modelo User.

class OrderFactory(factory.django.DjangoModelFactory): # criando uma fábrica para o modelo OrderItem, que é uma subclasse de DjangoModelFactory
    user = factory.SubFactory(UserFactory) # definindo o campo de usuário, que é um campo de texto, usando o método SubFactory do factory para criar um objeto de usuário usando a fábrica UserFactory.

    @factory.post_generation # definindo um método de pós-geração para o campo de produto, que é chamado após a criação do objeto de item de pedido.
    def product(self, create, extracted, **kwargs): # definindo o método de pós-geração para o campo de produto, que é chamado após a criação do objeto de item de pedido. O método recebe os parâmetros create, extracted e kwargs.
        if not create: # verificando se o objeto de item de pedido foi criado, se não foi criado, o método retorna sem fazer nada.
            return # se o objeto de item de pedido não foi criado, o método retorna sem fazer nada.

        if extracted: # verificando se o parâmetro extracted foi passado, se foi passado, o método adiciona os produtos passados ao campo de produto do objeto de item de pedido.
            for product in extracted: # iterando sobre os produtos passados no parâmetro extracted, que é uma lista de produtos.
                self.product.add(product) # adicionando o produto atual da iteração ao campo de produto do objeto de item de pedido.

    class Meta: # definindo a classe Meta para a fábrica, que é usada para configurar o comportamento da fábrica.
        model = Order # definindo o modelo que a fábrica irá usar, que é o modelo OrderItem.