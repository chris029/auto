class BaseCar:
    def __init__(self, price_min=20000, price_max=30000, make="base", model="car", fuel_type="petrol", generation=[]):

        self._price_min = price_min
        self._price_max = price_max
        self._make = make
        self._model = model
        self._generation = generation
        # self._engine_BHP_min = 90
        self._fuel_type = fuel_type
        # self._auto_transmission = ["automatic", "cvt", "dual-clutch", "semi-automatic", "automatic-stepless-sequential",
        #                            "automatic-stepless", "automatic-sequential", "automated-manual",
        #                            "direct-no-gearbox", ]
        # self._manual_transmission = ["manual", "manual-sequential", "automatic-sequential"]
        self._geographic_reach = 300

        self._main_search_url_model_based = f"https://www.otomoto.pl/osobowe/{self._make}/{self._model}/krakow/?" \
                                            f"search%5Bfilter_float_price%3Afrom%5D={self._price_min}" \
                                            f"&search%5Bfilter_float_price%3Ato%5D={self._price_max}" \
                                            f"&search%5Bfilter_enum_fuel_type%5D%5B0%5D={self._fuel_type}" \
                                            f"&search%5Bfilter_enum_damaged%5D=0" \
                                            f"&search%5Border%5D=created_at%3Adesc" \
                                            f"&search%5Bbrand_program_id%5D%5B0%5D=&search%5Bdist%5D={self._geographic_reach}&" \
                                            f"search%5Bcountry%5D=" + \
                                            ''.join(f"&search%5Bfilter_enum_generation%5D%5B{index}%5D={generation}"
                                                    for index, generation in enumerate(self._generation))

        self._main_search_url_type_based = f"https://www.otomoto.pl/osobowe/" \
                                           f"seg-compact--seg-coupe--seg-sedan/" \
                                           f"/od-2012/" \
                                           f"krakow/?" \
                                           f"search%5Bfilter_float_price%3Afrom%5D={self._price_min}" \
                                           f"&search%5Bfilter_float_price%3Ato%5D={self._price_max}" \
                                           f"&search%5Bfilter_enum_fuel_type%5D%5B0%5D={self._fuel_type}" \
                                           f"&search%5Bfilter_enum_damaged%5D=0" \
                                           f"&search%5Border%5D=created_at%3Adesc" \
                                           f"&search%5Bbrand_program_id%5D%5B0%5D=&search%5Bdist%5D={self._geographic_reach}&" \
                                           f"search%5Bcountry%5D="

    def get_car_model(self):
        return self._model

    # def get_main_url(self):
    #     return self._main_search_url

    def get_main_url(self):
        if self._is_make_or_model_selected() is True:
            return self._main_search_url_model_based
        else:
            return self._main_search_url_type_based

    def get_url_for_auto_transmission(self):
        return self._main_search_url + ''.join(
            [f"&search%5Bfilter_enum_gearbox%5D%5B{index}%5D={transmission_type}" for index, transmission_type in
             enumerate(self._auto_transmission)])

    def get_url_for_manual_transmission(self):
        return self._main_search_url + ''.join(
            [f"&search%5Bfilter_enum_gearbox%5D%5B{index}%5D={transmission_type}" for index, transmission_type in
             enumerate(self._manual_transmission)])

    def _is_make_or_model_selected(self):
        if self._make == "base" or self._model == "car":
            return False
        else:
            return True


class FordFiesta(BaseCar):
    def __init__(self):
        BaseCar.__init__(self, make="ford", model="fiesta",
                         generation=["gen-mk7-2008", "gen-mk8-2017"])


class ToyotaYaris(BaseCar):
    def __init__(self):
        BaseCar.__init__(self, make="toyota", model="yaris",
                         generation=["gen-iii-2011"])


class Mazda2(BaseCar):
    def __init__(self):
        BaseCar.__init__(self, make="mazda", model="2",
                         generation=["gen-iii-2015"])


class HyundaiI20(BaseCar):
    def __init__(self):
        BaseCar.__init__(self, make="hyundai", model="i20",
                         generation=["gen-ii-2014"])


class KiaRio(BaseCar):
    def __init__(self):
        BaseCar.__init__(self, make="kia", model="rio",
                         generation=["gen-iv-2017"])


class AutaPiotrka(BaseCar):
    def __init__(self):
        BaseCar.__init__(self)


class ToyotaAurisPetrol(BaseCar):
    def __init__(self):
        BaseCar.__init__(self, make="toyota", model="auris",
                         generation=["gen-ii-2012"])


class ToyotaAurisHybrid(BaseCar):
    def __init__(self):
        BaseCar.__init__(self,
                         make="toyota",
                         model="auris",
                         fuel_type="hybrid",
                         generation=["gen-ii-2012"])