from pizza import Pizza, PizzaSchoolCheesePizza, PizzaSchoolClamPizza, PizzaSchoolVeggiePizza
from pizza_store import PizzaStore, PizzaSchool


if __name__ == "__main__":
    pizzaschool: PizzaStore = PizzaSchool()

    pizza: Pizza = pizzaschool.order_pizza("cheese")
    print("내가 주문한 피자:", pizza.get())