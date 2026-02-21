import factory # importando o módulo de factory do Python, que é usado para criar objetos de teste de forma fácil e rápida.

from product.models import Product # importando o modelo Product do aplicativo product
from product.models import Category # importando o modelo Category do aplicativo product, que é usado para criar objetos de teste de categoria.

class CategoryFactory(factory.django.DjangoModelFactory): # criando uma fábrica para o modelo Category, que é uma subclasse de DjangoModelFactory
    title = factory.Faker("pystr") # definindo o campo de título, que é um campo de texto, usando o método Faker do factory para gerar um valor aleatório.
    slug = factory.Faker("pystr") # definindo o campo de slug, que é um campo de texto, usando o método Faker do factory para gerar um valor aleatório.
    description = factory.Faker("pystr") # definindo o campo de descrição, que é um campo de texto, usando o método Faker do factory para gerar um valor aleatório.
    active = factory.Iterator([True, False]) # definindo o campo de ativo, que é um campo booleano, usando o método Iterator do factory para gerar valores booleanos aleatórios.

    class Meta: # definindo a classe Meta para a fábrica, que é usada para configurar o comportamento da fábrica.
        model = Category # definindo o modelo que a fábrica irá usar, que é o modelo Category.

class ProductFactory(factory.django.DjangoModelFactory): # criando uma fábrica para o modelo Product, que é uma subclasse de DjangoModelFactory
    price = factory.Faker("pyint") # definindo o campo de preço, que é um campo decimal, usando o método Faker do factory para gerar um valor aleatório.
    # category = factory.LazyAttribute(CategoryFactory) # definindo o campo de categoria, que é uma lista de categorias, usando o método LazyAttribute do factory para criar um objeto de categoria usando a fábrica CategoryFactory.
    title = factory.Faker("pystr") # definindo o campo de título, que é um campo de texto, usando o método Faker do factory para gerar um valor aleatório.
    active = factory.Iterator([True, False]) # definindo o campo de ativo, que é um campo booleano, usando o método Iterator do factory para gerar valores booleanos aleatórios.

    @factory.post_generation # definindo um método de pós-geração para o campo de categoria, que é chamado após a criação do objeto de produto.
    def categories(self, create, extracted, **kwargs): # definindo o método de pós-geração para o campo de categoria, que é chamado após a criação do objeto de produto. O método recebe os parâmetros create, extracted e kwargs.
        if not create: # verificando se o objeto de produto foi criado, se não foi criado, o método retorna sem fazer nada.
            return # se o objeto de produto não foi criado, o método retorna sem fazer nada.

        if extracted: # verificando se o parâmetro extracted foi passado, se foi passado, o método adiciona as categorias passadas ao campo de categoria do objeto de produto.
            for cat in extracted: # iterando sobre as categorias passadas no parâmetro extracted, que é uma lista de categorias.
                self.category.add(cat) # adicionando a categoria atual da iteração ao campo de categoria do objeto de produto.
        else: 
            self.category.add(CategoryFactory()) # se o parâmetro extracted não foi passado, o método cria uma nova categoria usando a fábrica CategoryFactory e adiciona ao campo de categoria do objeto de produto.

    class Meta: # definindo a classe Meta para a fábrica, que é usada para configurar o comportamento da fábrica.
        model = Product # definindo o modelo que a fábrica irá usar, que é o modelo Product.