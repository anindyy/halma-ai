from abc import ABC, abstractmethod

class Agent(ABC):
    def __init__(self, id, _time):
        self.id = id
        self.time = _time

    @abstractmethod
    def play(self):
        pass
