from abc import ABC, abstractmethod
from subject_ import YoutubeChannel
from typing import List


class Observer(ABC):
    @abstractmethod
    def update(self, youtube: YoutubeChannel):
        pass


class ObserverA(Observer):
    def update(self, youtube: YoutubeChannel):
        if youtube < 2:
            print("observerA called")


class ObserverB(Observer):
    def update(self, youtube: YoutubeChannel):
        if youtube >= 3:
            print("observerB called")