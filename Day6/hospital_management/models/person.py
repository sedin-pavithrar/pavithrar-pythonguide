class Person:

    def __init__ (self,name:str,age:int,contact:str):
        self.__name = name
        self.__age = age
        self.__contact = contact 
     
    @property
    def name (self) -> str:
        return self.__name
    @property
    def age (self) -> int:
        return self.__age
    @property
    def contact (self)-> str:
        return self.__contact
    
    def __str__ (self)-> str:
        return f"{self.name} | {self.age}" 
    


    


    




        