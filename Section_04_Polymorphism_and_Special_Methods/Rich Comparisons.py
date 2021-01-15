def line_break():
    x = 0
    print("\n\n")
    while x < 20:
        print("*", end="")
        x += 1
    print("\n\n")


line_break()

from math import sqrt
from functools import total_ordering

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector(x={self.x}, y={self.y}'

v1 = Vector(0,0)
v2 = Vector(0, 0)
print(id(v1), id(v2))
print(v1 == v2)


line_break()

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector(x={self.x}, y={self.y}'

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return NotImplemented

v1 = Vector(0, 0)
v2 = Vector(0, 0)
v3 = Vector(10, 10)
print(id(v1), id(v2), id(v3))
print(v1 == v2, v1 is v2)
print(v1 == v3)


line_break()

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector(x={self.x}, y={self.y}'

    def __eq__(self, other):
        if isinstance(other, tuple):
            other = Vector(*other)
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return NotImplemented

v1 = Vector(10, 11)
print(v1 == (10, 11))
print((10, 11) == v1)


line_break()

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector(x={self.x}, y={self.y})'

    def __eq__(self, other):
        if isinstance(other, tuple):
            other = Vector(*other)
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return NotImplemented

    def __abs__(self):
        return  sqrt(self.x ** 2 + self.y ** 2)

    def __lt__(self, other):
        if isinstance(other, tuple):
            other = Vector(*other)
        if isinstance(other, Vector):
            return abs(self) < abs(other)
        return NotImplemented


v1 = Vector(0, 0)
v2 = Vector(1, 1)
print(repr(Vector))
print(repr(v1))
print(v1 < v2)
print(v2 > v1)
print(v1 < (1, 1))
print((1, 1) > v1)
print(v1, v2)
try:
    v1 <= v2
except TypeError as ex:
    print(ex)


line_break()

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector(x={self.x}, y={self.y})'

    def __eq__(self, other):
        if isinstance(other, tuple):
            other = Vector(*other)
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return NotImplemented

    def __abs__(self):
        return  sqrt(self.x ** 2 + self.y ** 2)

    def __lt__(self, other):
        if isinstance(other, tuple):
            other = Vector(*other)
        if isinstance(other, Vector):
            return abs(self) < abs(other)
        return NotImplemented

    def __le__(self, other):
        return self == other or self < other

v1 = Vector(0, 0)
v2 = Vector(0, 0)
v3 = Vector(1, 1)
print(v1 <= v2)
print(v1 <= v3)
print(v1 <= (0.5, 0.5))
print(v1 >= v2)
try:
    print(v1 != v2)
except TypeError as ex:
    print(ex)


line_break()

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector(x={self.x}, y={self.y})'

    def __eq__(self, other):
        print('__eq__ called...')
        if isinstance(other, tuple):
            other = Vector(*other)
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return NotImplemented

    def __abs__(self):
        print('__abs__ called...')
        return  sqrt(self.x ** 2 + self.y ** 2)

    def __lt__(self, other):
        print('__lt__ called...')
        if isinstance(other, tuple):
            other = Vector(*other)
        if isinstance(other, Vector):
            return abs(self) < abs(other)
        return NotImplemented

    def __le__(self, other):
        print('__le__ called...')
        return self == other or self < other

v1 = Vector(0, 0)
v2 = Vector(0, 0)
v3 = Vector(1, 1)
print(v1 <= v2)
print(v1 <= v3)
print(v1 <= (0.5, 0.5))
print(v1 >= v2)
try:
    print(v1 != v2)
except TypeError as ex:
    print(ex)


line_break()


@total_ordering
class Number:
    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        print('__eq__ called...')
        if isinstance(other, Number):
            return self.x == other.x
        return NotImplemented

    def __lt__(self, other):
        print('__lt__ called...')
        if isinstance(other, Number):
            return self.x < other.x
        return NotImplemented

a = Number(1)
b = Number(2)
c = Number(1)
d = 'a'

print(a < b)
print(a <= b)
print(a <= c)

try:
    print(a == d)
except:
    print("oops")