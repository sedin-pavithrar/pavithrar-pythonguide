Concepts Covered
Day 1–2
Variables
Data types
Strings
Conditionals
Loops
Dictionaries
Day 3
Modules (models)
Package imports
Day 4
HashMap (fleet dictionary)
Day 5
Problem decomposition and algorithm design
Day 6
Classes
Methods
Inheritance
Method overriding
super()
Encapsulation (_attributes)
@property
Polymorphism
Abstract classes (ABC, @abstractmethod)


@property 
turns a method into attribute 
without property
car.vehicle_id()
with property 
car.vehicle_id

ac tlike a senior developer and give me algm to do this and also include Day 1-2 Jun 9-10 Learn the Basics Variables, Data Types, Operators, Strings, 
Conditionals, Loops, Lists, Dicts
Day 3 Jun 11 Advanced Python Modules, Lambdas, Decorators, Iterators, Regular 
Expressions, Variable Scope
Day 4 Jun 12 DSA — Fundamentals Arrays, Linked Lists, HashMaps, Heaps, Stacks & 
Queues
Day 5 Jun 16 DSA — Advanced Binary Search, Recursion, Bubble/Merge/Quick 
Sort, Binary Search Tree
Day 6 Jun 17 Object Oriented 
Programming
Classes, Methods, Inheritance, Encapsulation, 
@property this topics whenever necessary
Vehicle Fleet System 
inheritance super() method overriding parent class
Real-world App
Ola / Uber / Rapido
Overview
Inheritance chain: Vehicle (base) defines trip_summary(). Child classes Car, Bike, Auto each 
override fare(distance) with their own base + per-km formula. Calling v.trip_summary() automatically
uses the correct child fare() -- polymorphism in action. This is how Ola and Uber switch between 
vehicle types in their pricing engine.
Problem
Base Vehicle class. Child classes Car, Bike, Auto each override fare(). trip_summary() defined 
once in Vehicle.
Fare Rates
Vehicle Base Fare Per KM 10 km Total
Car Rs.50 Rs.15 Rs.200
Bike Rs.20 Rs.8 Rs.100
Page 33 | Basics · DSA · OOP · Packages · Concurrency · Typing · Files · Formatting · Frameworks · Testing
Python Complete Assignments — Day 1 to Day 15 | roadmap.sh/python + 
roadmap.sh/backend/project-ideas
Auto Rs.30 Rs.10 Rs.130
Constraints
• Vehicle never instantiated directly
• fare() overridden in every child
• trip_summary() defined once in Vehicle
• Use super().__init__() in each child
Bonus: Add SurgePricedCar(Car) with 1.5x surge during peak hours.
what is this abc

abc stands for Abstract Base Classes.

It's a built-in Python module that lets you define blueprints for other classes.

You import it like this:

from abc import ABC, abstractmethod

There are two important things here:

ABC → makes a class abstract
@abstractmethod → marks methods that child classes must implement
Why use abc?

In your fleet system, you have this rule:

Vehicle should never be instantiated directly.

A generic vehicle doesn't make sense:

vehicle = Vehicle("V001", "Arun")

What kind of vehicle is it?

Car?
Bike?
Auto?

You don't know how to calculate its fare.

That's exactly what abstract classes prevent.

Without abc
class Vehicle:
    def fare(self, distance):
        pass

This allows:

v = Vehicle()

Calling:

v.fare(10)

returns None or causes unexpected errors later.

Python doesn't stop you.

With abc
from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def fare(self, distance):
        pass

Now this fails:

v = Vehicle()

Error:

TypeError: Can't instantiate abstract class Vehicle
with abstract method fare

Python enforces your design.

How ABC works

When you inherit from ABC:

class Vehicle(ABC):
    pass

Python knows:

"This class is incomplete and is meant only to be inherited."

How @abstractmethod works
class Vehicle(ABC):

    @abstractmethod
    def fare(self, distance):
        pass

Every child class must provide its own implementation.

For example:

class Car(Vehicle):

    def fare(self, distance):
        return 50 + distance * 15

If you forget:

class Car(Vehicle):
    pass

then:

car = Car()

raises:

TypeError: Can't instantiate abstract class Car
with abstract method fare
Your Fleet System Example
class Vehicle(ABC):

    @abstractmethod
    def fare(self, distance):
        pass

    def trip_summary(self, distance):
        total = self.fare(distance)
        return f"Fare: ₹{total}"

Child classes:

class Car(Vehicle):
    def fare(self, distance):
        return 50 + distance * 15


class Bike(Vehicle):
    def fare(self, distance):
        return 20 + distance * 8

Usage:

vehicles = [Car(), Bike()]

for v in vehicles:
    print(v.trip_summary(10))

Output:

Fare: ₹200
Fare: ₹100

Notice:

trip_summary() is written once.
fare() changes per vehicle.
Vehicle cannot be created directly.
Real-world analogy

Think of Vehicle as an architectural blueprint.

A blueprint says:

Every vehicle must have:

✓ a fare calculation method
✓ a trip summary

But the blueprint itself isn't a real vehicle.

You build:

Car
Bike
Auto

from that blueprint.

When should you use abc?

Use abstract classes when:

You want to enforce a common interface.
Some methods must be implemented by subclasses.
The parent class is incomplete by itself.
You want to prevent direct instantiation.

Examples:

Vehicle
PaymentMethod
Shape
NotificationService
DatabaseConnector

If every child class must implement something, abc is a good choice.

can this be of separate files

Yes. In fact, a senior developer would almost never keep all of these classes in a single file once the project starts growing.

A good rule:

One responsibility → one file
Related files → one package (folder)

For your fleet system, organize it like this:

vehicle_fleet/
│
├── main.py
├── models/
│   ├── __init__.py
│   ├── vehicle.py
│   ├── car.py
│   ├── bike.py
│   ├── auto.py
│   └── surge_priced_car.py
│
└── utils/
    ├── __init__.py
    └── validators.py
models/vehicle.py

Define the abstract base class.

from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(
        self,
        vehicle_id: str,
        driver_name: str,
        base_fare: float,
        per_km_rate: float
    ):
        self._vehicle_id = vehicle_id
        self._driver_name = driver_name
        self._base_fare = base_fare
        self._per_km_rate = per_km_rate

    @abstractmethod
    def fare(self, distance: float) -> float:
        pass

    def trip_summary(self, distance: float) -> str:
        total = self.fare(distance)
        return f"{self._vehicle_id}: ₹{total}"
models/car.py
from models.vehicle import Vehicle


class Car(Vehicle):

    def __init__(self, vehicle_id: str, driver_name: str):
        super().__init__(vehicle_id, driver_name, 50, 15)

    def fare(self, distance: float) -> float:
        return self._base_fare + distance * self._per_km_rate
models/bike.py
from models.vehicle import Vehicle


class Bike(Vehicle):

    def __init__(self, vehicle_id: str, driver_name: str):
        super().__init__(vehicle_id, driver_name, 20, 8)

    def fare(self, distance: float) -> float:
        return self._base_fare + distance * self._per_km_rate
models/auto.py
from models.vehicle import Vehicle


class Auto(Vehicle):

    def __init__(self, vehicle_id: str, driver_name: str):
        super().__init__(vehicle_id, driver_name, 30, 10)

    def fare(self, distance: float) -> float:
        return self._base_fare + distance * self._per_km_rate
models/surge_priced_car.py
from models.car import Car


class SurgePricedCar(Car):

    def __init__(
        self,
        vehicle_id: str,
        driver_name: str,
        surge_multiplier: float = 1.5
    ):
        super().__init__(vehicle_id, driver_name)
        self._surge_multiplier = surge_multiplier

    def fare(self, distance: float) -> float:
        normal_fare = super().fare(distance)
        return normal_fare * self._surge_multiplier
main.py
from models.car import Car
from models.bike import Bike
from models.auto import Auto
from models.surge_priced_car import SurgePricedCar


fleet = {
    "CAR101": Car("CAR101", "Arun"),
    "BIKE201": Bike("BIKE201", "Kumar"),
    "AUTO301": Auto("AUTO301", "Ravi"),
    "SURGE401": SurgePricedCar("SURGE401", "Priya")
}

for vehicle in fleet.values():
    print(vehicle.trip_summary(10))
Why the __init__.py files?

They tell Python:

"This folder is a package."

Even though newer Python versions can work without them in some cases, keeping them is a good practice.

They can be empty:

# models/__init__.py
Optional improvement

You can simplify imports by exporting classes from models/__init__.py.

from .car import Car
from .bike import Bike
from .auto import Auto
from .surge_priced_car import SurgePricedCar

Then main.py becomes:

from models import Car, Bike, Auto, SurgePricedCar

As projects grow, this structure scales well:

models/       → business objects
services/     → business logic
utils/        → helpers
tests/        → unit tests
config/       → settings

Separating files like this makes your code easier to:

maintain
test
debug
extend
collaborate on with a team
give me whole code 

Here's a complete implementation using a multi-file project structure.

Project Structure
vehicle_fleet/
│
├── main.py
│
├── models/
│   ├── __init__.py
│   ├── vehicle.py
│   ├── car.py
│   ├── bike.py
│   ├── auto.py
│   └── surge_priced_car.py
models/vehicle.py
from abc import ABC, abstractmethod


class Vehicle(ABC):
    """Abstract base class for all vehicle types."""

    def __init__(
        self,
        vehicle_id: str,
        driver_name: str,
        base_fare: float,
        per_km_rate: float,
    ):
        self._vehicle_id = vehicle_id
        self._driver_name = driver_name
        self._base_fare = base_fare
        self._per_km_rate = per_km_rate

    @property
    def vehicle_id(self) -> str:
        return self._vehicle_id

    @property
    def driver_name(self) -> str:
        return self._driver_name

    @property
    def base_fare(self) -> float:
        return self._base_fare

    @property
    def per_km_rate(self) -> float:
        return self._per_km_rate

    @abstractmethod
    def fare(self, distance: float) -> float:
        """Calculate the total fare."""
        pass

    def trip_summary(self, distance: float) -> str:
        if distance <= 0:
            raise ValueError("Distance must be greater than zero.")

        total_fare = self.fare(distance)

        return (
            f"{self.__class__.__name__} | "
            f"Vehicle ID: {self.vehicle_id} | "
            f"Driver: {self.driver_name} | "
            f"Distance: {distance} km | "
            f"Fare: ₹{total_fare:.2f}"
        )

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self.vehicle_id})"
models/car.py
from models.vehicle import Vehicle


class Car(Vehicle):

    def __init__(self, vehicle_id: str, driver_name: str):
        super().__init__(
            vehicle_id=vehicle_id,
            driver_name=driver_name,
            base_fare=50,
            per_km_rate=15,
        )

    def fare(self, distance: float) -> float:
        return self.base_fare + (distance * self.per_km_rate)
models/bike.py
from models.vehicle import Vehicle


class Bike(Vehicle):

    def __init__(self, vehicle_id: str, driver_name: str):
        super().__init__(
            vehicle_id=vehicle_id,
            driver_name=driver_name,
            base_fare=20,
            per_km_rate=8,
        )

    def fare(self, distance: float) -> float:
        return self.base_fare + (distance * self.per_km_rate)
models/auto.py
from models.vehicle import Vehicle


class Auto(Vehicle):

    def __init__(self, vehicle_id: str, driver_name: str):
        super().__init__(
            vehicle_id=vehicle_id,
            driver_name=driver_name,
            base_fare=30,
            per_km_rate=10,
        )

    def fare(self, distance: float) -> float:
        return self.base_fare + (distance * self.per_km_rate)
models/surge_priced_car.py
from models.car import Car


class SurgePricedCar(Car):

    def __init__(
        self,
        vehicle_id: str,
        driver_name: str,
        surge_multiplier: float = 1.5,
    ):
        super().__init__(vehicle_id, driver_name)
        self._surge_multiplier = surge_multiplier

    @property
    def surge_multiplier(self) -> float:
        return self._surge_multiplier

    def fare(self, distance: float) -> float:
        normal_fare = super().fare(distance)
        return normal_fare * self.surge_multiplier
models/__init__.py
from .car import Car
from .bike import Bike
from .auto import Auto
from .surge_priced_car import SurgePricedCar

__all__ = ["Car", "Bike", "Auto", "SurgePricedCar"]
main.py
from models import Car, Bike, Auto, SurgePricedCar


def main():
    fleet = {
        "CAR101": Car("CAR101", "Arun"),
        "BIKE201": Bike("BIKE201", "Kumar"),
        "AUTO301": Auto("AUTO301", "Ravi"),
        "SURGE401": SurgePricedCar("SURGE401", "Priya"),
    }

    distance = 10

    print("\n=== Trip Summaries ===\n")

    for vehicle in fleet.values():
        print(vehicle.trip_summary(distance))


if __name__ == "__main__":
    main()
Expected Output
=== Trip Summaries ===

Car | Vehicle ID: CAR101 | Driver: Arun | Distance: 10 km | Fare: ₹200.00

Bike | Vehicle ID: BIKE201 | Driver: Kumar | Distance: 10 km | Fare: ₹100.00

Auto | Vehicle ID: AUTO301 | Driver: Ravi | Distance: 10 km | Fare: ₹130.00

SurgePricedCar | Vehicle ID: SURGE401 | Driver: Priya | Distance: 10 km | Fare: ₹300.00
Concepts Covered
Day 1–2
Variables
Data types
Strings
Conditionals
Loops
Dictionaries
Day 3
Modules (models)
Package imports
Day 4
HashMap (fleet dictionary)
Day 5
Problem decomposition and algorithm design
Day 6
Classes
Methods
Inheritance
Method overriding
super()
Encapsulation (_attributes)
@property
Polymorphism
Abstract classes (ABC, @abstractmethod)
explain every file line by line 

Excellent. Reading code line by line is how senior engineers learn unfamiliar codebases.

Let's walk through the project file by file.

Project Structure
vehicle_fleet/
│
├── main.py
│
├── models/
│   ├── __init__.py
│   ├── vehicle.py
│   ├── car.py
│   ├── bike.py
│   ├── auto.py
│   └── surge_priced_car.py
1. models/vehicle.py

This is the foundation of the entire system.

from abc import ABC, abstractmethod
abc = Abstract Base Classes module.
ABC makes a class abstract.
@abstractmethod forces child classes to implement certain methods.
class Vehicle(ABC):

Create an abstract class named Vehicle.

Because it inherits from ABC, you cannot do:

vehicle = Vehicle(...)

This enforces the rule:

Every vehicle must be a Car, Bike, or Auto.

def __init__(
    self,
    vehicle_id: str,
    driver_name: str,
    base_fare: float,
    per_km_rate: float,
):

Constructor parameters:

self → current object
vehicle_id → unique identifier
driver_name → driver's name
base_fare → fixed fare
per_km_rate → cost per kilometer

Type hints improve readability.

self._vehicle_id = vehicle_id
self._driver_name = driver_name
self._base_fare = base_fare
self._per_km_rate = per_km_rate

Store values inside the object.

The leading underscore (_) means:

Protected attribute

It's a convention saying:

Don't access these directly outside the class.

Properties

Instead of:

car._base_fare

use:

car.base_fare

through properties.

@property
def vehicle_id(self) -> str:
    return self._vehicle_id

@property turns a method into an attribute.

Without property:

car.vehicle_id()

With property:

car.vehicle_id


Abstract Method
@abstractmethod
def fare(self, distance: float) -> float:
    pass

Every child class must implement this method.

Python prevents creating a child class that forgets to define fare().


Vehicle
│
├── Encapsulation
│   ├── _base_fare
│   ├── _driver_name
│   └── @property
│
├── Inheritance
│   ├── Car
│   ├── Bike
│   └── Auto
│
└── Polymorphism
    └── fare()


| Concept       | Focus                              | Example                   |
| ------------- | ---------------------------------- | ------------------------- |
| Encapsulation | Hiding data                        | `_base_fare`, `@property` |
| Inheritance   | Reusing code                       | `class Car(Vehicle)`      |
| Polymorphism  | Same interface, different behavior | `vehicle.fare(10)`        |
