from abc import ABC, abstractmethod

#Abstract base Class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Concrete subclass  
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side
    

# my_shape = Shape()  # This would raise a TypeError
sq = Square(5)
print(sq.area())      # Output: 25    