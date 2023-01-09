from abc import ABC, abstractmethod
from typing import List


class Observer(ABC):
    
    @abstractmethod
    def update(self):
        pass


class ObserverA(Observer):
    def update(self):
        print("observerA called")


class ObserverB(Observer):
    def update(self):
        print("observerB called")