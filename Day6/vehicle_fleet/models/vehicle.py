from abc import ABC , abstractmethod

# Abstract Base Class 
class Vehicle(ABC):
    def __init__(self, vehicle_id:str,
            driver_name:str,
            base_fare:float,
            per_km_rate:float ):
        #protected attributes dont use these directly outside class 
        self._vehicle_id = vehicle_id 
        self._driver_name = driver_name
        self._base_fare = base_fare
        self._per_km_rate = per_km_rate

    @property #turns a method into attribute 
    def vehicle_id(self) -> str:
        return self._vehicle_id
    
    @property
    def driver_name(self) -> str:
        return self._driver_name
    
    @property
    def base_fare(self) -> float:
        return self._base_fare
    
    @property
    def per_km_rate(self)->float:
        return self._per_km_rate
    
    @abstractmethod 
    def fare(self,distance:float) -> float:
        pass
    

    def trip_summary(self,distance:float)-> str:

        if distance <= 0:
            raise ValueError("Distance must be greater than zero")
        
        total = self.fare(distance) 

        #self can be Car Bike Auto which Python calls the correct method -> polymorphism 
        
        return (f"{self.__class__.__name__} | " 
    f"Vehicle ID: {self.vehicle_id} | "
    f"Driver: {self.driver_name} | "
    f"Distance: {distance} km | "
    f"Fare: ₹{total:.2f}"
    )

def __str__(self) -> str:
        return f"{self.__class__.__name__}({self.vehicle_id})"

        




""" abc = Abstract Base Classes module  built-in module used to define common interfaces and enforce structural rules across a group of related classes.

ABC makes a class abstract. 

An Abstract Base Class (ABC) cannot be instantiated directly. 
Instead, it acts as a blueprint or contract, requiring any subclass that inherits from it to implement specific methods.
If a subclass fails to implement these required methods, Python throws a TypeError the moment you try to create an object from it.

@abstractmethod forces child classes to implement certain methods.


"""

# Abstract classes serve as a strict blueprint for other classes. 
# They are necessary because they dictate a mandatory set of methods that any child class must implement.
#  If a developer tries to use a normal base class, there is no built-in enforcement, and critical features may be forgotten.
#  Why You Can't "Just Use It Normally"If you try to create a standard, everyday parent class, 
 
# it causes two main problems:
# Accidental Instantiation: 
# You can accidentally create an object of the incomplete parent class. 
#     For example, if you have a base Shape class but forget to create a Circle or Square, you might mistakenly try to call Shape.draw(), which does nothing or crashes. 
#     Abstract classes cannot be instantiated. Python will throw an error, preventing you from using an incomplete object.
    
# Missing Implementations: 
# With normal classes, a child class can inherit the parent's code but completely forget to add its own specific versions of required methods.'


# 'Why We Use Abstract Classes InsteadThey Establish an Enforced Contract: 
# 'By using the abc module and the @abstractmethod decorator, you force any child class to write its own logic for that specific method. '
# 'If the child class doesn't, Python will throw a TypeError when you try to use it.
# They Prevent Code Duplication: You can write complete, fully-functioning helper methods inside the abstract class that all child classes can share, while safely leaving the specific, changing parts as abstract methods.
# They Make Code Reliable: As the GeeksforGeeks guide explains, abstract classes ensure that derived classes are always consistent and complete.