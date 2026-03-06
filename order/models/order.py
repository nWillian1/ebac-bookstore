from django.contrib.auth.models import (
    User,
)  # importando o modelo de usuário do Django
from django.db import models  # importando o módulo de modelos do Django

from product.models.product import (
    Product,
)  # importando o modelo de produto para criar relacionamento entre pedido e produto


class Order(models.Model):  #  definindo a classe Order que herda de models.Model
    product = models.ManyToManyField(
        Product, blank=False
    )  #  definindo um campo de relacionamento de várias categorias, campo obrigatório.
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False
    )  # definindo um campo de relacionamento de chave estrangeira para o modelo de usuário, campo obrigatório.
