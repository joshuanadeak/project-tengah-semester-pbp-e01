from django.test import TestCase
from django.urls import reverse, resolve
from stock.views import *

# Create your tests here.


class TestUrls(TestCase):
    def test_show_market_url(self):
        url = reverse("stock:show_market")
        self.assertEqual(resolve(url).func, show_market)

    def test_show_stock_url(self):
        url = reverse("stock:show_stock")
        self.assertEqual(resolve(url).func, show_stock)

    def test_mjson_url(self):
        url = reverse("stock:show_market_json")
        self.assertEqual(resolve(url).func, show_market_json)

    def test_porto_njson_url(self):
        url = reverse("stock:show_note_json")
        self.assertEqual(resolve(url).func, show_note_json)

    def test_add_url(self):
        url = reverse("stock:add_stock")
        self.assertEqual(resolve(url).func, add_stock)

    def test_porto_add_note_url(self):
        url = reverse("stock:add_note")
        self.assertEqual(resolve(url).func, add_note)

    def test_delete_market_url(self):
        url = reverse("stock:delete_market", kwargs={"market_id": 1})
        self.assertEqual(resolve(url).func, delete_market)

    def test_delete_stock_url(self):
        url = reverse("stock:delete_stock", kwargs={"stock_id": 1})
        self.assertEqual(resolve(url).func, delete_stock)

    def test_json_url(self):
        url = reverse("stock:show_stock_json")
        self.assertEqual(resolve(url).func, show_stock_json)
