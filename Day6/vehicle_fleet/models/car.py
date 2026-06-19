from models.vehicle import Vehicle

class Car(Vehicle): 
    def __init__(self,
            vehicle_id:str,
            driver_name:str
                 ):
        # Vehicle.__init__()
        super().__init__(
            vehicle_id,
            driver_name,
            base_fare=50,
            per_km_rate=15
            )
    
    #Override 
    def fare(self,distance:float)-> float:
        return self._base_fare + distance * self._per_km_rate
    
