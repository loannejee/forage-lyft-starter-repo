"""
Serviceable is an abstract class which is a blueprint for its child classes. It allows you to create a set of methods that must be created within any child classes built from the abstract class.
"""
from serviceable import Serviceable


class Car(Serviceable):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        if (self.engine.needs_service() or self.battery.needs_service()):
            return True
