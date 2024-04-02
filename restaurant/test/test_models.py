import decimal
from django.test import TestCase
from restaurant import models


class MenuTestCase(TestCase):

    model = models.Menu

    def test_get_menu(self):
        item = self.model.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")

    def test_update_menu(self):

        item = self.model.objects.create(title="Salad", price=12.3, inventory=120)
        item.title = "Salad2"
        item.price = decimal.Decimal(8.99)
        item.inventory = 119

        self.assertEqual(item.title, "Salad2")
        self.assertEqual(item.price, decimal.Decimal(8.99))
        self.assertEqual(item.inventory, 119)
