#P - 번

class Vector2D:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)
