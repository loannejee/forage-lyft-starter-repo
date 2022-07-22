from tire.tire import Tire


# Octoprime tires should be serviced only when the sum of all values in the 
# tire wear array is greater than or equal to 3. 
class OctoprimeTires(Tire):
    def __init__(self, tire_wear_array):
        self.tire_wear_array = tire_wear_array

    def needs_service(self):
        sum = sum(self.tire_wear_array)
        if sum >= 3:
            return True
        else:
            return False 