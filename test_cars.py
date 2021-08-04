import unittest
import requests
from bs4 import BeautifulSoup
from search_engine import SearchEngine
from cars import BaseCar, FordFiesta


class TestBaseCar(unittest.TestCase):
    _base_car = BaseCar()
    _ford_fiesta = FordFiesta()

    def test_link_generation_type(self):
        self.assertFalse(TestBaseCar._base_car._is_make_or_model_selected())

    def test_link_generation_model(self):
        self.assertTrue(TestBaseCar._ford_fiesta._is_make_or_model_selected())