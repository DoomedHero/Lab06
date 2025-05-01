from ftplib import parse150

from point import Point

class Line:
    """Represents a line segment defined by two points"""
    def __init__(self, p1:Point, p2:Point):
        self.p1 = p1
        self.p2 = p2

    def getPoint(self, end: int) -> Point:
        if end == 2:
            return self.p2
        else:
            return self.p1

    def translate(selfself, dx, dy, end: int):
        if end == 2:
            return self.__p2.translate(dx, dy)
        else:
            return self.__p1.translate(dx, dy)

    def __str__(self):
        return f'Line({self.p1}, {self.p2})'

def main():
    l = Line(Point(5,5), Point(3 , 3))
    print(l.translate (1,1, end=1))

if __name__ == '__main__':
    main()