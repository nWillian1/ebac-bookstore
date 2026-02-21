from django.test import TestCase
from product.factories import ProductFactory

class TestProductModel(TestCase):
    def setUp(self):
        self.product = ProductFactory(title="Teclado Mecânico")

    def test_product_creation(self):
        """Verifica se o produto é criado com o título correto"""
        self.assertEqual(self.product.title, "Teclado Mecânico")
        self.assertTrue(self.product.active) 