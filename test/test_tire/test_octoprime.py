import unittest

from tire.octoprime import OctoprimeTire

# Octoprime tires should be serviced only when the sum of all values in the 
# tire wear array is greater than or equal to 3. 
class TestCapuletEngine(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear_array = [0.75, 0.95, 0.89, 0.91]
        # sum = 3.50
        tire = OctoprimeTire(tire_wear_array)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        tire_wear_array = [0.55, 0.23, 0.89, 0.75]
        # sum = 2.42
        tire = OctoprimeTire(tire_wear_array)
        self.assertFalse(tire.needs_service())