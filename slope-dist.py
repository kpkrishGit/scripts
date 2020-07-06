import sys
import math
from ast import literal_eval

class Line:
    def __init__(self, coordinate1, coordinate2):
        self.coordinate1 = coordinate1
        self.coordinate2 = coordinate2

    def distance(self):
        """
        distance = math.sqrt((y2-y1)^2 + (x2-x1)^2
        """
        x1,y1 = self.coordinate1
        x2,y2 = self.coordinate2
        return(math.sqrt((y2-y1)**2 + (x2-x1)**2))

    def slope(self):
        """
        slope = (y2-y1) / (x2 -x1)
        """
        x1,y1 = self.coordinate1
        x2,y2 = self.coordinate2
        return((y2-y1)/(x2-x1))


if __name__ == '__main__':
    c1 = literal_eval(sys.argv[1])
    c2 = literal_eval(sys.argv[2])

    print(c1, c2)
    l1 = Line(c1, c2)
    print(l1.distance())
    print(l1.slope())
