from django.test import TestCase
from product.factories import ProductFactory
from order.factories import OrderFactory
from order.serializers import OrderSerializer

class TestOrderSerializer(TestCase):
    def setUp(self):
        self.product_1 = ProductFactory(price=100)
        self.product_2 = ProductFactory(price=250)
        
        self.order = OrderFactory()
        
        self.order.product.add(self.product_1, self.product_2)
        
        self.serializer = OrderSerializer(self.order)

    def test_order_serializer_total_calculation(self):
        data = self.serializer.data
        
        self.assertEqual(data["total"], 350)
        
    def test_order_serializer_product_count(self):
        data = self.serializer.data
        self.assertEqual(len(data["product"]), 2)