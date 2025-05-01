class Point:
    """Represents a point in 2d space."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point({self.x}, {self.y})'

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy