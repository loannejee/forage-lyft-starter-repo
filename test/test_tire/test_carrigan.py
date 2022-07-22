import unittest

from tire.carrigan import CarriganTires

# Carrigan tires should be serviced only when one or more of the values in the
# tire wear array is greater than or equal to 0.9. 
class TestCapuletEngine(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear_array = [0.55, 0.23, 0.89, 0.9]
        # checked_tire_array = [0, 0, 0, 1]
        tires = CarriganTires(tire_wear_array)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        tire_wear_array = [0.55, 0.23, 0.89, 0.75]
        # checked_tire_array = [0, 0, 0, 0]
        tires = CarriganTires(tire_wear_array)
        self.assertFalse(tires.needs_service())