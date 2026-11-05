# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        if type(width) != int or type(height) != int:
            raise TypeError()
        if width <= 0 or height <= 0:
            raise ValueError()
        # Add code here to check type and value of provided width & height,
        # raising appropriate exceptions if necessary (see README.md)
        self.width = width
        self.height = height    
    def is_square(self):
        """ If square return True, otherwise False """
        if self.width == self.height:
            return True
        else:
            return False
    def area(self):
        """ Returns area of object as int """
        return (self.width*self.height)
    def perimeter(self):
        """Return perimeter of object as int"""
        return ((self.width * 2) + (self.height * 2))
    # Implement methods is_square(), area() & perimeter() here
    # (See README.md for details of what they should do)
"""James = Rectangle(10,10)
print(James.area())"""