from django.db import models  # Criando o modelo de produto para a aplicação

from .category import (
    Category,
)  # Importando o modelo de categoria para criar relacionamento entre produto e categoria


class Product(
    models.Model
):  # Modelo de produto com campos para título, descrição, preço e estoque
    title = models.CharField(max_length=100)  # Título do produto, campo obrigatório
    description = models.TextField(
        max_length=500, blank=True, null=True
    )  # Descrição do produto, campo opcional
    price = models.PositiveBigIntegerField(
        null=True
    )  # Preço do produto, campo opcional
    active = models.BooleanField(
        default=True
    )  # Campo para indicar se o produto está ativo
    category = models.ManyToManyField(
        Category, blank=True
    )  # Relacionamento de várias categorias, campo opcional

    def __str__(
        self,
    ):  # Método para retornar o título do produto como representação em string
        return self.title  # Retorna o título do produto como representação em string.
