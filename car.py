"""
Serviceable is an abstract class, the blueprint for Car. It allows you to create a set of methods that must be created within any child classes built from the abstract class.

Car will be used to instantiate new car objects. __init__() should be included.

"""
from serviceable import Serviceable

# Car is the SubClass of Serviceable. 
# It is also whole/parent to compositions/children: Engine and Battery
class Car(Serviceable):
    def __init__(self, engine, battery, tire):
        self.engine = engine
        self.battery = battery
        self.tire = tire

    def needs_service(self):
        if (self.engine.needs_service() or self.battery.needs_service() or self.tire.needs_service()):
            return True