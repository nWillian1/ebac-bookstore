from rest_framework import serializers # importando o módulo de serializers do Django Rest Framework

from product.models.category import Category # importando o modelo Category do aplicativo product

class CategorySerializer(serializers.ModelSerializer): # criando um serializer para o modelo Category, que é uma subclasse de ModelSerializer
    class Meta: # definindo a classe Meta para o serializer, que é usada para configurar o comportamento do serializer.
        model = Category # definindo o modelo que o serializer irá usar, que é o modelo Category.
        fields = [ # definindo os campos que o serializer irá usar, que são o campo de título, slug, descrição e ativo.
            "title", # definindo o campo de título, que é um campo de texto.
            "slug", # definindo o campo de slug, que é um campo de texto.
            "description", # definindo o campo de descrição, que é um campo de texto.
            "active", # definindo o campo de ativo, que é um campo booleano.
        ]
        extra_kwargs = {"slug": {"required": False}} # definindo os campos extras para o serializer, que é usado para configurar o comportamento dos campos do serializer. Neste caso, o campo de produto é definido como não obrigatório.