from abc import ABC, abstractmethod

class Serviceable(ABC):
    """ 
    All classes have a function called __init__(), which is always executed when the class is being initiated.

    The __init__() function is called automatically every time the class is being used to create a new object.
    """

    def __init__(self):
        pass
    
    # Every class needs to have this method
    @abstractmethod
    def needs_service(self):
        pass