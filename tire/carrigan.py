from tire.tire import Tire


# Carrigan tires should be serviced only when one or more of the values in the
# tire wear array is greater than or equal to 0.9. 
class CarriganTires(Tire):
    def __init__(self, tire_wear_array):
        self.tire_wear_array = tire_wear_array

    def needs_service(self):
        def tire_checker(num):
            if num >= 0.9:
                return 1
            else:
                return 0
            
        checked_tire_array = map(tire_checker, self.tire_wear_array)
        sum = sum(checked_tire_array)
        if sum > 0:
            return True
        else:
            return False 


    """
    Model Answer:
    
    def needs_service(self):
        for tire in self.tire_wear:
            if tire >= 0.9:
                return True
        return False

    """
    
