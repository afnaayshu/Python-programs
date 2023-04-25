#abstract class demo using class polygon
from abc import ABC,abstractmethod

class Polygon(ABC):
    @abstractmethod
    def no_ofSides(self):
        pass
    
class Triangle(Polygon):
    #overriding
    def no_ofSides(self):
        print("3 sides")

class Pentagon(Polygon):
    def no_ofSides(self):
        print("5 sides")

class Heptagon(Polygon):
    def no_ofSides(self):
        print("7 sides")

class Nonagon(Polygon):
    def no_ofSides(self):
        print("9 sides")

T =Triangle()
T.no_ofSides()

P =Pentagon()
P.no_ofSides()

H =Heptagon()
H.no_ofSides()

N =Nonagon()
N.no_ofSides()
