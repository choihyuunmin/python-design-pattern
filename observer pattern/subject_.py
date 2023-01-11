from abc import ABC, abstractmethod
from typing import List
import random

class Subject(ABC):
    @abstractmethod
    def register_observer(self, obeserver):
        pass

    @abstractmethod
    def remove_observer(self, observer):
        pass

    @abstractmethod
    def notify_observer(self, observer):
        pass


class YoutubeChannel(Subject):
    _observers: List =  []
    concept_num = None

    def register_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observer(self, concept_num):
        for observer in self._observers:
            observer.update(concept_num)

    def new_video(self):
        concept_num = random.randrange(1, 6)

        print(f"새 영상이 업로드 되었습니다. 분야는 {concept_num}번 입니다.")
        self.notify_observer(concept_num)