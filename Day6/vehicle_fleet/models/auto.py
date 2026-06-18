from models.vehicle import Vehicle

class Auto(Vehicle):
    def __init__(self,vehicle_id:str,driver_name:str):
        super().__init__(vehicle_id,driver_name,base_fare=30,per_km_rate=10)

    def fare(self,distance:float)-> float:
        return self._base_fare + distance * self._per_km_rate
    
    