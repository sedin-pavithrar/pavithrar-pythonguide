from models.person import Person

class Doctor(Person):
    def __init__ (self,name:str,age:int,contact:str,specialisation:str ,fee:float ):

        super().__init__( 
            name,
            age,
            contact)
        
        self._specialisation = specialisation
        self.__fee = fee

    @property
    def specialisation (self) -> str:
        return self._specialisation

    @property
    def fee (self) -> float:
        return self.__fee
    




    