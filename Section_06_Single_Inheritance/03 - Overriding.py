def line_break():
    x = 0
    print("\n\n")
    while x < 20:
        print("*", end="")
        x += 1
    print("\n\n")

line_break()

class Person:
    pass

p = Person()
print(f"str(p): {str(p)}")

line_break()

class Person:
    def __str__(self):
        return 'Person class'

p = Person()
print(f"str(p): {str(p)}")

line_break()

class Person():
    def __repr__(self):
        return 'Person()'

p = Person()
print(f"str(p): {str(p)}")

line_break()

class Shape:
    def __init__(self, name):
        self.name = name

    def info(self):
        return f'Shape.info called for Shape({self.name})'

    def extended_info(self):
        return f'Shape.extended_info called for Shape({self.name})'

class Polygon(Shape):
    def __init__(self, name):
        self.name = name  # we'll come back to this later in the context of using super()

    def info(self):
        return f'Polygon info called for Polygon({self.name})'

p = Polygon('square')
print(f'p.info(): {p.info()}')
print(f'p.extended_info(): {p.extended_info()}')

line_break()

class Shape:
    def __init__(self, name):
        self.name = name

    def info(self):
        return f'Shape.info called for Shape({self.name})'

    def extended_info(self):
        return f'Shape.extended_info called for Shape({self.name})', self.info()

class Polygon(Shape):
    def __init__(self, name):
        self.name = name  # we'll come back to this later in the context of using super()

    def info(self):
        return f'Polygon info called for Polygon({self.name})'

p = Polygon('Square')
print(f"p.info(): {p.info()}")
print(f'p.extended_info(): {p.extended_info()}')

line_break()

class Person:
    def __str__(self):
        return 'Person.__str__ called'

class Student(Person):
    def __repr__(self):
        return 'Student.__repr__ called'

s = Student()
print(f"str(s): {str(s)}")
print(f"repr(s): {repr(s)}")

line_break()

class Person:
    def __str__(self):
        print("Person.__str__ called...")
        return self.__repr__()

class Student(Person):
    def __repr__(self):
        return 'Student.__repr__ called...'

s = Student()
print(f"str(s): {str(s)}")
print(f"repr(s): {repr(s)}")

line_break()
class Person:
    def __str__(self):
        print("Person.__str__ called...")
        return self.__repr__()

class Student(Person):
    def __repr__(self):
        return 'Student.__repr__ called...'

s = Student()
print(f"str(s): {str(s)}")
print(f"repr(s): {repr(s)}")
