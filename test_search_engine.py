import unittest
import requests
from bs4 import BeautifulSoup
from search_engine import SearchEngine
from cars import FordFiesta

fiesta = FordFiesta()


class TestParametersScraping(unittest.TestCase):
    test_link = "https://www.otomoto.pl/oferta/ford-fiesta-jak-nowa-ID6Dlcti.html#9d19372767"
    single_offer = requests.get(test_link)
    single_offer_soup = BeautifulSoup(single_offer.content, features="html.parser")

    def test_bhp_value(self):
        # data from the test link
        BHP = 85

        self.assertEqual(BHP,
                         SearchEngine(fiesta)._get_engine_bhp(
                             TestParametersScraping.single_offer_soup))

    def test_year_of_production(self):
        # data from the test link
        year_of_production = 2019

        self.assertEqual(year_of_production,
                         SearchEngine(fiesta)._get_year_of_production(
                             TestParametersScraping.single_offer_soup))

    def test_mileage(self):
        # data from the test link
        mileage = 7500

        self.assertEqual(mileage,
                         SearchEngine(fiesta)._get_mileage(
                             TestParametersScraping.single_offer_soup))

    def test_transmission(self):
        # data from the test link
        transmission = "Manualna"

        self.assertEqual(transmission,
                         SearchEngine(fiesta)._get_transmission(
                             TestParametersScraping.single_offer_soup))

    def test_number_of_doors(self):
        # data from the test link
        number_of_doors = 5

        self.assertEqual(number_of_doors,
                         SearchEngine(fiesta)._get_number_of_doors(
                             TestParametersScraping.single_offer_soup))

    def test_offer_holder(self):
        # data from the test link
        offer_holder = "Firmy"

        self.assertEqual(offer_holder,
                         SearchEngine(fiesta)._get_offer_holder(
                             TestParametersScraping.single_offer_soup))

    def test_version(self):
        # data from the link
        version = "1.1 Trend"

        self.assertEqual(version,
                         SearchEngine(fiesta)._get_version(
                             TestParametersScraping.single_offer_soup))

    def test_origin(self):
        # data from the link
        origin = None

        self.assertEqual(origin,
                         SearchEngine(fiesta)._get_origin(
                             TestParametersScraping.single_offer_soup))

    def test_first_owner(self):
        # data from link
        first_owner = None

        self.assertEqual(first_owner,
                         SearchEngine(fiesta)._get_first_owner(
                             TestParametersScraping.single_offer_soup))

    def test_car_make(self):
        # data from link
        car_make = "Ford"

        self.assertEqual(car_make,
                         SearchEngine(fiesta)._get_car_make(
                             TestParametersScraping.single_offer_soup))

    def test_car_model(self):
        # data from link
        car_model = "Ford"

        self.assertEqual(car_model,
                         SearchEngine(fiesta)._get_car_make(
                             TestParametersScraping.single_offer_soup))