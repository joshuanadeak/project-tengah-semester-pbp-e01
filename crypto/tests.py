from django.test import TestCase
from crypto.models import *
from django.urls import reverse, resolve
from crypto.views import *
from django.contrib.auth.models import User

# Create your tests here.
class CryptoTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="dummy", password="dummy")
        self.crypto = Crypto.objects.create(user=self.user, kode_crypto="DUM", nama_crypto="Dummy", harga_crypto="5000", risk="LOW")
        self.market = Market.objects.create(kode_crypto="DUM", nama_crypto="Dummy", harga_crypto="5000", risk="LOW")
        self.notes = Notes.objects.create(user=self.user, note="Test")
    
    def test_crypto_user(self):
        self.assertEqual(self.crypto.user, self.user)
    
    def test_notes_user(self):
        self.assertEqual(self.notes.user, self.user)

    def test_show_market_url(self):
        url = reverse("crypto:show_market")
        self.assertEqual(resolve(url).func, show_market)

    def test_show_stock_url(self):
        url = reverse("crypto:show_crypto")
        self.assertEqual(resolve(url).func, show_crypto)

    def test_mjson_url(self):
        url = reverse("crypto:show_market_json")
        self.assertEqual(resolve(url).func, show_market_json)

    def test_porto_njson_url(self):
        url = reverse("crypto:show_notes_json")
        self.assertEqual(resolve(url).func, show_notes_json)

    def test_add_url(self):
        url = reverse("crypto:add_crypto")
        self.assertEqual(resolve(url).func, add_crypto)

    def test_porto_add_note_url(self):
        url = reverse("crypto:add_note")
        self.assertEqual(resolve(url).func, add_note)

    def test_delete_market_url(self):
        url = reverse("crypto:delete_market", kwargs={"market_id": 1})
        self.assertEqual(resolve(url).func, delete_market)

    def test_delete_crypto_url(self):
        url = reverse("crypto:delete_crypto", kwargs={"stock_id": 1})
        self.assertEqual(resolve(url).func, delete_crypto)

    def test_json_url(self):
        url = reverse("crypto:show_crypto_json")
        self.assertEqual(resolve(url).func, show_crypto_json)