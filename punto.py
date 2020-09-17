import math
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def hallarDistancia(self,punto):
        p = math.sqrt(math.pow(self.x-punto.x,2) + math.pow(self.y-punto.y,2))
        return p

p1 = Punto(2.5,4.2)
p2 = Punto(3.5,5.2)

p1.hallarDistancia(p2)

