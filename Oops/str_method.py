class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __str__(self):  # string representation of the object
        return f"Rectangle with length={self.length}and width={self.width}"


rect = Rectangle(6, 8)
print(rect.__str__())


"""
@classmethod
@staticmethod
"""
