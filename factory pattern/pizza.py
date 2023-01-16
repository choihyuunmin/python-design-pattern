from abc import ABC, abstractmethod
from typing import List

class Pizza(ABC):
    name: str
    dough: str
    sauce: str
    toppings = []

    def prepare(self) -> None:
        print(f"준비중: {self.name}")
        print("도우 돌리는중")
        print("소스 뿌리는중")
        print("토핑 올리는중")

        for topping in self.toppings:
            print(" " + topping)

    def bake(self) -> None:
        print("175도에서 25분 굽기")
        
    def cut(self) -> None:
        print("피자를 사선으로 자르기")

    def box(self) -> None:
        print("포장하기")

    def get(self) -> str:
        return self.name

    
class PizzaSchoolCheesePizza(Pizza):
    def __init__(self):
        self.name = "피자스쿨 치즈 피자"
        self.dough = "씬 크러스트 도우"
        self.sauce = "치즈 소스"

        self.toppings.append("크림치즈")


class PizzaSchoolVeggiePizza(Pizza):
    def __init__(self):
        self.name = "피자스쿨 베지피자"
        self.dough = "두꺼운 크러스트 도우"
        self.sauce = "칠리 소스"

        self.toppings.append("모짜렐라 치즈")

    def cut(self) -> None:
        print("네모난 모양으로 자르기")


class PizzaSchoolClamPizza(Pizza):
    def __init__(self):
        self.name = "피자스쿨 클램피자"
        self.dough = "쫀득한 도우"
        self.sauce = "스위트 칠리 소스"

        self.topping.append("아메리칸 치즈")
        self.topping.append("고구마")