from car import Car
from abc import ABC, abstractmethod

class Battery(Car, ABC):
    def __init__(self):
        pass

    @abstractmethod
    def needs_service(self):
        pass