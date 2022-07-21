from battery.battery import Battery
import datetime

class Nubbin(Battery):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date # 2017
        self.next_service_date = self.last_service_date.replace(year=self.last_service_date.year + 4) # 2021

    def needs_service(self):
        if (datetime.date.today() > self.next_service_date): # 2022 > 2021
            return True
        else:
            return False