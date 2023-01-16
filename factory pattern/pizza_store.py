from abc import ABC, abstractmethod
from typing import Union
from pizza import Pizza, PizzaSchoolCheesePizza, PizzaSchoolClamPizza, PizzaSchoolVeggiePizza

class PizzaStore(ABC):

    @abstractmethod
    def create_pizza(self, type: str):
        pass
    
    def order_pizza(self, type: str) -> Pizza:
        pizza: Pizza = self.create_pizza(type)
        
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza
    

class PizzaSchool(PizzaStore):
    def create_pizza(self, item: str) -> Union[Pizza, None]:
        if item == "cheese":
            return PizzaSchoolCheesePizza()
        elif item == "veggie":
            return PizzaSchoolVeggiePizza()
        elif item == "clam":
            return PizzaSchoolClamPizza()
        else:
            return