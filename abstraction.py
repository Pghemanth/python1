#abstraction
from abc import ABC


class car:

    def __init__(self,name,mileage,price,color):
        self.name=name
        self.maileage=maileage
        self.price=price
        self.color=color
        self.speed=0

class Supre(car):
    pass

class Bmw(car):
    pass

c1=Supra("supra mk4",784554,"black")   
c2=Bmw("bmw",487998,"black")     