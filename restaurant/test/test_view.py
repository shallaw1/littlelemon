from django.test import TestCase
from django.urls import reverse
from restaurant import models
from user.models import User


class MenuViewSetTestCase(TestCase):
    model = models.Menu

    def setUp(self) -> None:
        self.list_url_name = 'menu-list'
        self.detail_url_name = 'menu-detail'
        self.menu_items = [
            {'title': 'Ice Cream', 'price': '3.40', 'inventory': 109},
            {'title': 'Salad', 'price': '13.10', 'inventory': 99},
            {'title': 'Drinks', 'price': '4.00', 'inventory': 111},
            {'title': 'Apetizers', 'price': '16.32', 'inventory': 110},
        ]

        for item in self.menu_items:
            self.model.objects.create(**item)

        user = User.objects.create(username="admin", email="admin@admin.com")
        self.client.force_login(user)

        return super().setUp()

    def test_get_all(self):
        res = self.client.get(reverse(self.list_url_name))
        response_data = [
            {"title": r["title"], "price": r["price"], "inventory": r["inventory"]}
            for r in res.json()
        ]

        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(response_data), 4)
        self.assertEqual(response_data, self.menu_items)
