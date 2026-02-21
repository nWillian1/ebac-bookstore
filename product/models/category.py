from django.db import models # Criando o modelo de produto para a aplicação

class Category(models.Model): # Modelo de categoria com campos para título, slug, descrição e ativo
    title = models.CharField(max_length=100) # Título da categoria, campo obrigatório
    slug = models.SlugField(unique=True) # Slug da categoria, campo obrigatório e único
    description = models.CharField(max_length=200, blank=True, null=True) # Descrição da categoria, campo opcional
    active = models.BooleanField(default=True) # Campo para indicar se a categoria está ativa.

    def __unicode__(self): # Método para retornar o título da categoria como representação em string
        return self.title # Retorna o título do produto como representação em string.