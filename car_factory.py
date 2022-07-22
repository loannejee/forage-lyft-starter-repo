from battery.nubbin import Nubbin
from battery.spindler import Spindler
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from tire.carrigan import CarriganTires
from tire.octoprime import OctoprimeTires

class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_array):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = Spindler(current_date, last_service_date)
        tires = CarriganTires(tire_wear_array)
        car = Car(engine, battery, tires)
        return car

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_array):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = Spindler(current_date, last_service_date)
        tires = OctoprimeTires(tire_wear_array)
        car = Car(engine, battery, tires)
        return car

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_is_on, tire_wear_array):
        engine = SternmanEngine(warning_light_is_on)
        battery = Spindler(current_date, last_service_date)
        tires = CarriganTires(tire_wear_array)
        car = Car(engine, battery, tires)
        return car

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_array):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = Nubbin(current_date, last_service_date)
        tires = OctoprimeTires(tire_wear_array)
        car = Car(engine, battery, tires)
        return car

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_array):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = Nubbin(current_date, last_service_date)
        tires = CarriganTires(tire_wear_array)
        car = Car(engine, battery, tires)
        return car