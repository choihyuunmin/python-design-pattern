from abc import ABC, abstractmethod
from typing import List
from observer import Observer


class Subject(ABC):
    
    @abstractmethod
    def register_observer(self, obeserver: Observer):
        pass

    @abstractmethod
    def remove_observer(self, observer: Observer):
        pass

    @abstractmethod
    def notify_observer(self, observer: Observer):
        pass


class ConcreteSubject(Subject):
    _observers: List[Observer]= []

    def register_observer(self, observer: Observer):
        self._observers.append(observer)

    def remove_observer(self, observer: Observer):
        self._observers.remove(observer)

    def notify_observer(self):
        for observer in self._observers:
            observer.update()

    def change_measurements(self):
        self.notify_observer()