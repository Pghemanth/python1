
from abc import ABC,abstractmethod


class car(ABC):

    def __init__(self,name,price,color):
        self.name=name
        self.price=price
        self.color=color
        self.speed=0

    @abstractmethod
    def stop():
        pass
    @abstractmethod
    def speed_up():
        pass
    @abstractmethod
    def speed_down():
        pass

class Bmw(car):
    def speed_up(self):
        self.speed+=5
    def speed_down(self):
        self.speed-=5
    def stop(self):
        self.speed=0
class Tata(car):
    def speed_up(self):
        self.speed+=2
    def speed_down(self):
        self.speed-=2
    def stop(self):
        self.speed=0 


bmw=Bmw ('mk4','black',469996)   
nexon=Tata("nexon ev",487998,"white")     