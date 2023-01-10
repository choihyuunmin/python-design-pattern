from subject_ import YoutubeChannel
from observer_ import ObserverA, ObserverB


subject = YoutubeChannel()

observer_a = ObserverA()
subject.register_observer(observer_a)

observer_b = ObserverB()
subject.register_observer(observer_b)


# subject.remove_observer(observer_a)
subject.new_video()