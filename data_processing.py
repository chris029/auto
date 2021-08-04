import matplotlib.pyplot as plt
# print(plt.get_backend())

import pandas as pd
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
pd.set_option('display.width', 420)
pd.set_option('display.max_colwidth', None)

from search_engine import SearchEngine


class DataProcessing:
    def __init__(self):
        pass

    def plot_optimal_sorting(self, filename):
        all_cars_dataframe = pd.read_csv(filename, index_col=0)
        all_cars_dataframe = all_cars_dataframe.loc[(all_cars_dataframe['BHP'] >= 0) &
                                                    (all_cars_dataframe['Mileage'] <= 200000) &
                                                    (all_cars_dataframe['Year'] >= 2000) &
                                                    (all_cars_dataframe['Year'] <= 2021)]\
            .sort_values(['Year', 'BHP', 'Price'], ascending=[False, False, True])\
            .reset_index(drop=True)
        all_cars_dataframe.to_excel("samochody.xlsx", index=False)
        print(all_cars_dataframe.sort_values(['Year', 'BHP', 'Price'], ascending=[False, False, True]))

    def plot_single_car_data(self, car_object, update=False):
        print(self._pick_data_frame(car_object, update))

    def update_all_car_data(self):
        # takes all available car_xxx.csv data and combines it into one all_car_data.csv
        try:
            df_2 = pd.read_csv("car_2.csv")
            df_fiesta = pd.read_csv("car_fiesta.csv")
            df_i20 = pd.read_csv("car_i20.csv")
            df_rio = pd.read_csv("car_rio.csv")
            df_yaris = pd.read_csv("car_yaris.csv")

            all_cars = [df_2, df_fiesta, df_i20, df_rio, df_yaris]
            df_all_cars = pd.concat(all_cars, ignore_index=True)
            df_all_cars.to_csv("all_cars.csv")

        except FileNotFoundError as e:
            print(f"At least one file is missing: {e.filename}")

    def plot_all_car_data(self):
        print(pd.read_csv("all_cars.csv", index_col=0))

    def plot_histogram(self, car_object, update=False, block=False):
        data_frame = self._pick_data_frame(car_object, update)
        bins = list(range(20000, 41000, 1000))
        labels = [str(item)[0:-3] for item in bins]

        plt.figure(figsize=(6, 2))
        plt.hist(data_frame.Price, bins=bins, color='#abcdef')
        plt.title(car_object.get_car_model())
        plt.xticks(bins, labels=labels)
        plt.show(block=block)

    @staticmethod
    def _pick_data_frame(car_object, update_flag):
        # grab a file name based on a car object
        file_name = "car_" + car_object.get_car_model() + ".csv"

        # check if a csv file is present
        try:
            assert update_flag is False
            # if so, use it to plot data of a car
            return pd.read_csv(file_name)

        except (FileNotFoundError, AssertionError):
            # if not, generate one using a search engine
            # if 'update_flag' is True update a file
            df = pd.DataFrame(SearchEngine(car_object).get_car_info_from_website())
            df.to_csv(file_name, index=False)
            return pd.read_csv(file_name)