def line_break():
    x = 0
    print("\n\n")
    while x < 20:
        print("*", end="")
        x += 1
    print("\n\n")

line_break()

class Shape:
    pass

class Ellipse(Shape):
    pass

class Circle(Ellipse):
    pass

class Polygon(Shape):
    pass

class Rectangle(Polygon):
    pass

class Square(Rectangle):
    pass

class Triangle(Polygon):
    pass

print("issubclass(Ellipse, Shape): "+ str(issubclass(Ellipse, Shape)))

s = Shape()
e = Ellipse()
try:
    print(issubclass(e, s))
except TypeError as ex:
    print(ex)
print("isinstance(e, Ellipse): " + str(isinstance(e, Ellipse)))
print("isinstance(e, Shape): " + str(isinstance(e, Shape)))
print("issubclass(Square, Shape): " + str(issubclass(Square, Shape)))
sq = Square()
print("isinstance(sq, Square): " + str(isinstance(sq, Square)))
print("isinstance(sq, Rectangle): " + str(isinstance(sq, Rectangle)))
print("isinstance(sq, Polygon): " + str(isinstance(sq, Polygon)))
print("isinstance(sq, Shape): " + str(isinstance(sq, Shape)))
print("issubclass(Square, Ellipse): " + str(issubclass(Square, Ellipse)))
print("isinstance(sq, Ellipse): " + str(isinstance(sq, Ellipse)))

line_break()

class Person:
    pass

print("issubclass(Person, object): " + str(issubclass(Person, object)))
p = Person()
print("isinstance(p, Person): " + str(isinstance(p, Person)))

line_break()

print("issubclass(Square, object): " + str(issubclass(Square, object)))
print("isinstance(sq, object): " + str(isinstance(sq, object)))