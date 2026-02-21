from django.test import TestCase
from product.factories import CategoryFactory, ProductFactory
from product.serializers.product_serializer import ProductSerializer

class TestProductSerializer(TestCase):
    def setUp(self):
        self.category = CategoryFactory(title="eletronicos")
        self.product = ProductFactory(title="mouse", price=100)
        self.product.category.add(self.category)
        self.serializer = ProductSerializer(self.product)

    def test_product_serializer_fields(self):
        """Verifica se os campos do JSON estão corretos"""
        data = self.serializer.data
        self.assertEqual(data["title"], "mouse")
        self.assertEqual(data["price"], 100)
        self.assertEqual(data["category"][0]["title"], "eletronicos")