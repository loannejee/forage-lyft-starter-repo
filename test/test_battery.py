import unittest
from datetime import datetime

from battery.nubbin import Nubbin
from battery.spindler import Spindler

# Nubbin Battery - should be serviced once every 4 years
class TestNubbin(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)
        battery = Nubbin(current_date, last_service_date)
        self.assertTrue(battery.needs_service())
    
    def test_battery_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        battery = Nubbin(current_date, last_service_date)
        self.assertFalse(battery.needs_service())


# Spindler Battery - should be serviced once every 2 years
class TestSpindler(unittest.TestCase):
    def test1_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)
        battery = Spindler(current_date, last_service_date)
        self.assertTrue(battery.needs_service())
    
    # last_service_date = 2020-07-20
    # date_which_battery_should_be_serviced_by = 2022-07-20
    # one day later
    def test2_battery_should_be_serviced(self):
        current_date = datetime.today().date() # 2022-07-21
        last_service_date = current_date.replace(year=current_date.year - 2, day=current_date.day - 1)
        battery = Spindler(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test1_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)
        battery = Spindler(current_date, last_service_date)
        self.assertFalse(battery.needs_service())
    
    # last_service_date = 2020-07-22
    # date_which_battery_should_be_serviced_by = 2022-07-22
    # one day before
    def test2_battery_should_not_be_serviced(self):
        current_date = datetime.today().date() # 2022-07-21
        last_service_date = current_date.replace(year=current_date.year - 2, day=current_date.day + 1)
        battery = Spindler(current_date, last_service_date)
        self.assertFalse(battery.needs_service())

    