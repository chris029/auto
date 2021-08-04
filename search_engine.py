from bs4 import BeautifulSoup
import requests


class SearchEngine:
    def __init__(self, car_object):
        self.car_info_dict = {"Make": [],
                              "Model": [],
                              "Price": [],
                              "BHP": [],
                              "Year": [],
                              "Mileage": [],
                              "Transmission": [],
                              "Number of doors": [],
                              "Offered by": [],
                              "Version": [],
                              "Origin": [],
                              "First owner": [],
                              "offer_url": []}

        self._main_url = car_object.get_main_url()
        self._main_http = requests.get(self._main_url)
        self._car_model = car_object.get_car_model()

    def get_car_info_from_website(self):
        self._get_offer_urls()

        outdated_links = []
        number_of_offers = len(self.car_info_dict["offer_url"])
        for index, offer_url in enumerate(self.car_info_dict["offer_url"]):
            single_offer = requests.get(offer_url)
            single_offer_soup = BeautifulSoup(single_offer.content, features="html.parser")

            try:
                print(f"Collecting data for {self._car_model}: {index}/{number_of_offers}")
                # price has to be first in order to properly raise exceptions if a page is outdated
                self.car_info_dict["Price"].append(self._get_prices(single_offer_soup))
                self.car_info_dict["BHP"].append(self._get_engine_bhp(single_offer_soup))
                self.car_info_dict["Year"].append(self._get_year_of_production(single_offer_soup))
                self.car_info_dict["Mileage"].append(self._get_mileage(single_offer_soup))
                self.car_info_dict["Transmission"].append(self._get_transmission(single_offer_soup))
                self.car_info_dict["Number of doors"].append(self._get_number_of_doors(single_offer_soup))
                self.car_info_dict["Offered by"].append(self._get_offer_holder(single_offer_soup))
                self.car_info_dict["Version"].append(self._get_version(single_offer_soup))
                self.car_info_dict["Origin"].append(self._get_origin(single_offer_soup))
                self.car_info_dict["First owner"].append(self._get_first_owner(single_offer_soup))
                self.car_info_dict["Make"].append(self._get_car_make(single_offer_soup))
                self.car_info_dict["Model"].append(self._get_car_model(single_offer_soup))

            except AttributeError:
                print(f"The offer {offer_url} is outdated.")
                outdated_links.append(offer_url)
                continue

        for link in outdated_links:
            self.car_info_dict["offer_url"].remove(link)

        return self.car_info_dict

    @staticmethod
    def _get_prices(soup):
        price_tag = soup.find("div", class_="offer-price")
        return int(price_tag.get("data-price").replace(",","").replace(" ", ""))

    @staticmethod
    def _get_engine_bhp(soup):
        parameters_list = soup.find_all("li", class_="offer-params__item")
        for parameter in parameters_list:
            if parameter.find("span", class_="offer-params__label").get_text() == "Moc":
                return int(parameter.find("div", class_="offer-params__value").get_text().split()[0])

    @staticmethod
    def _get_year_of_production(soup):
        parameters_list = soup.find_all("li", class_="offer-params__item")
        for parameter in parameters_list:
            if parameter.find("span", class_="offer-params__label").get_text() == "Rok produkcji":
                return int(parameter.find("div", class_="offer-params__value").get_text())

    @staticmethod
    def _get_mileage(soup):
        parameters_list = soup.find_all("li", class_="offer-params__item")
        for parameter in parameters_list:
            if parameter.find("span", class_="offer-params__label").get_text() == "Przebieg":
                return int("".join(parameter.find("div", class_="offer-params__value").get_text().split()[0:-1]))

    @staticmethod
    def _get_transmission(soup):
        parameters_list = soup.find_all("li", class_="offer-params__item")
        for parameter in parameters_list:
            if parameter.find("span", class_="offer-params__label").get_text() == "Skrzynia biegów":
                return parameter.find("div", class_="offer-params__value").get_text().strip()

    @staticmethod
    def _get_number_of_doors(soup):
        parameters_list = soup.find_all("li", class_="offer-params__item")
        for parameter in parameters_list:
            if parameter.find("span", class_="offer-params__label").get_text() == "Liczba drzwi":
                return int(parameter.find("div", class_="offer-params__value").get_text())

    @staticmethod
    def _get_offer_holder(soup):
        parameters_list = soup.find_all("li", class_="offer-params__item")
        for parameter in parameters_list:
            if parameter.find("span", class_="offer-params__label").get_text() == "Oferta od":
                return parameter.find("div", class_="offer-params__value").get_text().strip()

    @staticmethod
    def _get_version(soup):
        parameters_list = soup.find_all("li", class_="offer-params__item")
        for parameter in parameters_list:
            if parameter.find("span", class_="offer-params__label").get_text() == "Wersja":
                return parameter.find("div", class_="offer-params__value").get_text().strip()

    @staticmethod
    def _get_origin(soup):
        parameters_list = soup.find_all("li", class_="offer-params__item")
        for parameter in parameters_list:
            if parameter.find("span", class_="offer-params__label").get_text() == "Kraj pochodzenia":
                return parameter.find("div", class_="offer-params__value").get_text().strip()

    @staticmethod
    def _get_first_owner(soup):
        parameters_list = soup.find_all("li", class_="offer-params__item")
        for parameter in parameters_list:
            if parameter.find("span", class_="offer-params__label").get_text() == "Pierwszy właściciel":
                return parameter.find("div", class_="offer-params__value").get_text().strip()

    @staticmethod
    def _get_car_make(soup):
        parameters_list = soup.find_all("li", class_="offer-params__item")
        for parameter in parameters_list:
            if parameter.find("span", class_="offer-params__label").get_text() == "Marka pojazdu":
                return parameter.find("div", class_="offer-params__value").get_text().strip()

    @staticmethod
    def _get_car_model(soup):
        parameters_list = soup.find_all("li", class_="offer-params__item")
        for parameter in parameters_list:
            if parameter.find("span", class_="offer-params__label").get_text() == "Model pojazdu":
                return parameter.find("div", class_="offer-params__value").get_text().strip()

    def _get_offer_urls(self):
        max_page = self._get_number_of_pages()

        for page_number in range(0, max_page):
            print(f"Gathering urls from page: {page_number}/{max_page}")
            page_number += 1

            single_page = requests.get(self._main_url + f"&page={page_number}")
            url_soup = BeautifulSoup(single_page.content, features="html.parser")

            offers = url_soup.find_all("h2")
            for offer in offers:
                self.car_info_dict["offer_url"].append(offer.find("a").get("href"))

    def _get_number_of_pages(self):
        page_nums = [1]
        page_numbers_soup = BeautifulSoup(self._main_http.content, features="html.parser")

        page_nums_as_string = page_numbers_soup.find_all("span", class_="page")

        for element in page_nums_as_string:
            try:
                page_nums.append(int(element.get_text()))
            except ValueError:
                # used to drop the '...' link from the list of page numbers
                pass

        return max(page_nums)
