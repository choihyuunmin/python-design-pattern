from abc import ABC, abstractmethod
from typing import List

class Strategy(ABC):
    @abstractmethod
    def do_something(self, data: List):
        pass

class Context:
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def do_something_in_context(self) -> None:
        self._strategy.do_something()



class ConcreteStrategyA(Strategy):
    def do_something(self) -> None:
        print("strategy A is running")

class ConcreteStrategyB(Strategy):
    def do_something(self) -> None:
        print("strategy B is running")



if __name__ == "__main__":
    context = Context(ConcreteStrategyA())
    context.do_something_in_context()

    context.strategy = ConcreteStrategyB()
    context.do_something_in_context()