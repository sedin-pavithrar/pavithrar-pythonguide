from models.person import Person
class Patient(Person):

    def __init__ (self,name:str,age:int,contact:str):

        super().__init__(
            name,
            age,
            contact
        )
        self.__appointments = []
        
    @property
    def appointments (self) -> list:
            return self.__appointments.copy() # prevents outside code from modifying the list directly.
        
    def add_appointments (self,appointment:dict) -> None:
            self.__appointments.append(appointment)
            

