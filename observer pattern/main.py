from subject import ConcreteSubject
from observer import ObserverA, ObserverB


subject = ConcreteSubject()

observer_a = ObserverA()
subject.register_observer(observer_a)

observer_b = ObserverB()
subject.register_observer(observer_b)


subject.remove_observer(observer_a)
subject.change_measurements()