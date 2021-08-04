from data_processing import DataProcessing
from cars import *

# fiesta = FordFiesta()
# yaris = ToyotaYaris()
# mazda = Mazda2()
# hyundai = HyundaiI20()
# kia = KiaRio()

# DataProcessing().plot_single_car_data(fiesta)
# DataProcessing().plot_single_car_data(yaris)
# DataProcessing().plot_single_car_data(mazda)
# DataProcessing().plot_single_car_data(hyundai)
# DataProcessing().plot_single_car_data(kia)
# DataProcessing().update_all_car_data()
# DataProcessing().plot_optimal_sorting("all_cars.csv")

auta_piotrka = AutaPiotrka()
print(auta_piotrka.get_main_url())
DataProcessing().plot_single_car_data(auta_piotrka)
DataProcessing().plot_optimal_sorting("car_car.csv")
