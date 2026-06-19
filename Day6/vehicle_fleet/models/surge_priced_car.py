from car import Car

class SurgePricedCar(Car):
    def __init__(
            self,
            vehicle_id:str,
            driver_name:str,
            surge_multiplier:float = 1.5
    ):
        super().__init__(vehicle_id,driver_name)            #Call Car's constructor.# Car's constructor already calls Vehicle's constructor.

        self.__surge_multiplier = surge_multiplier  # SurgePricedCar -> Car -> Vehicle



    @property #read only 
    def surge_multiplier(self) -> float:
        return self.__surge_multiplier

    def fare (self,distance:float)-> float:
        normal_fare = super().fare(distance)
        return normal_fare * self.surge_multiplier
