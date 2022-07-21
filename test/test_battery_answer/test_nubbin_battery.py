import unittest
from datetime import date

from battery.nubbin import Nubbin


# Nubbin Battery - should be serviced once every 4 years
class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2016-01-25")
        # date_which_battery_should_be_serviced_by = 2020-01-25
        battery = Nubbin(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2019-01-10")
        # date_which_battery_should_be_serviced_by = 2023-01-10
        battery = Nubbin(current_date, last_service_date)
        self.assertFalse(battery.needs_service())