def line_break():
    x = 0
    print("\n\n")
    while x < 20:
        print("*", end="")
        x += 1
    print("\n\n")


line_break()

class Int:
    def __init__(self, min_value=None, max_value=None):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner_class, name):
        self.name = name

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError(f'{self.name} must be an int.')
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f'{self.name} must be at least {self.min_value}')
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f'{self.name} cannot exceed {self.max_value}')
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return instance.__dict__.get(self.name, None)

class Point2D:
    x = Int(min_value=0, max_value=800)
    y = Int(min_value=0, max_value=400)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point2D(x={self.x}, y={self.y})'

    def __str__(self):
        return f'({self.x}, {self.y})'

p = Point2D(0, 10)
print(f'str(p) = {str(p)}')
print(f'repr(p) = {repr(p)}')
print(f'p.x , p.y = {p.x} , {p.y}')

try:
    p = Point2D(0, 500)
except ValueError as ex:
    print(ex)

line_break()

import collections
import collections.abc

print(f'isinstance([1, 2, 3], collections.abc.Sequence) = '
      f'{isinstance([1, 2, 3], collections.abc.Sequence)}')
print(f'isinstance([1, 2, 3], collections.abc.MutableSequence) = '
      f'{isinstance([1, 2, 3], collections.abc.MutableSequence)}')
print(f'isinstance((1, 2, 3), collections.abc.Sequence) = '
      f'{isinstance((1, 2, 3), collections.abc.Sequence)}')
print(f'isinstance((1, 2, 3), collections.abc.MutableSequence) = '
      f'{isinstance((1, 2, 3), collections.abc.MutableSequence)}')

line_break()

class Point2DSequence:
    def __init__(self, min_length=None, max_length=None):
        self.min_length = min_length
        self.max_length = max_length

    def __set_name__(self, cls, name):
        self.name = name

    def __set__(self, instance, value):
        if not isinstance(value, collections.abc.Sequence):
            raise ValueError(f'{self.name} must be a Sequence type.')
        if self.min_length is not None and len(value) < self.min_length:
            raise ValueError(f'{self.name} must contain at least {self.min_length} elements')
        if self.max_length is not None and len(value) > self.max_length:
            raise ValueError(f'{self.name} cannot contain more than {self.max_length} elements')
        for index, item in enumerate(value):
            if not isinstance(item, Point2D):
                raise ValueError(f'Item at index {index} is not a Point2D instance.')

        # value passes checks - want to store it as a mutable sequence so we can append to it later
        instance.__dict__[self.name] = list(value)

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            if self.name not in instance.__dict__:
                # Current point list has not been defined
                # so let's create an empty list
                instance.__dict__[self.name] = []
            return instance.__dict__.get(self.name)

class Polygon:
    vertices = Point2DSequence(min_length=3)

    def __init__(self, *vertices):
        self.vertices = vertices

try:
    p = Polygon()
except ValueError as ex:
    print(ex)

try:
    p = Polygon(Point2D(-100,0), Point2D(0,1), Point2D(1,0))
except ValueError as ex:
    print(ex)

p = Polygon(Point2D(0, 0), Point2D(0, 1), Point2D(1, 0))
print(f'p.vertices = {p.vertices}')

line_break()

class Polygon:
    vertices = Point2DSequence(min_length=3)

    def __init__(self, *vertices):
        self.vertices = vertices

    def append(self, pt):
        if not isinstance(pt, Point2D):
            raise ValueError('Can only append Point2D instances.')
        max_length = type(self).vertices.max_length
        if max_length is not None and len(self.vertices) >= max_length:
            # cannot add more points!
            raise ValueError(f'Vertices length is at max ({max_length})')
        self.vertices.append(pt)

p = Polygon(Point2D(0,0), Point2D(1,0), Point2D(0, 1))
print(f'p.vertices = {p.vertices}')
p.append(Point2D(10, 10))
print(f'p.vertices = {p.vertices}')

line_break()

class Polygon:
    vertices = Point2DSequence(min_length=3, max_length=3)

    def __init__(self, *vertices):
        self.vertices = vertices

    def append(self, pt):
        if not isinstance(pt, Point2D):
            raise ValueError('Can only append Point2D instances.')
        max_length = type(self).vertices.max_length
        if max_length is not None and len(self.vertices) >= max_length:
            # cannot add more points!
            raise ValueError(f'Vertices length is at max ({max_length})')
        self.vertices.append(pt)

p = Polygon(Point2D(0,0), Point2D(1,0), Point2D(0, 1))

try:
    p.append(Point2D(10, 10))
except ValueError as ex:
    print(ex)

line_break()

class Polygon:
    vertices = Point2DSequence(min_length=3)

    def __init__(self, *vertices):
        self.vertices = vertices

    def append(self, pt):
        if not isinstance(pt, Point2D):
            raise ValueError('Can only append Point2D instances.')
        max_length = type(self).vertices.max_length
        if max_length is not None and len(self.vertices) >= max_length:
            # cannot add more points!
            raise ValueError(f'Vertices length is at max ({max_length})')
        self.vertices.append(pt)

class Triangle(Polygon):
    vertices = Point2DSequence(min_length=3, max_length=3)

p = Polygon(Point2D(0,0), Point2D(1,0), Point2D(0,1))
p.append(Point2D(10, 10))
print(f'p.vertices = {p.vertices}')

t = Triangle(Point2D(0,0), Point2D(1,0), Point2D(0,1))
try:
    t.append(Point2D(10, 10))
except ValueError as ex:
    print(ex)

class Square(Polygon):
    vertices = Point2DSequence(min_length=4, max_length=4)

s = Square(Point2D(0,0), Point2D(1,0), Point2D(0,1), Point2D(1, 1))
print(f's.vertices = {s.vertices}')

try:
    s.append(Point2D(10, 10))
except ValueError as ex:
    print(ex)

line_break()

class Polygon:
    vertices = Point2DSequence(min_length=3)

    def __init__(self, *vertices):
        self.vertices = vertices

    def append(self, pt):
        if not isinstance(pt, Point2D):
            raise ValueError('Can only append Point2D instances.')
        max_length = type(self).vertices.max_length
        if max_length is not None and len(self.vertices) >= max_length:
            # cannot add more points!
            raise ValueError(f'Vertices length is at max ({max_length})')
        self.vertices.append(pt)

    def __len__(self):
        return len(self.vertices)

    def __getitem__(self, idx):
        return self.vertices[idx]

p = Polygon(Point2D(0, 0), Point2D(1, 0), Point2D(1, 1))
print(f'len(p) = {len(p)}')
print(f'list(p) = {list(p)}')
print(f'p[0] , p[1] , p[2] = {p[0] , p[1] , p[2]}')
print(f'p[0:2] = {p[0:2]}')

line_break()

class Polygon:
    vertices = Point2DSequence(min_length=3)

    def __init__(self, *vertices):
        self.vertices = vertices

    def append(self, pt):
        if not isinstance(pt, Point2D):
            raise ValueError('Can only append Point2D instances.')
        max_length = type(self).vertices.max_length
        if max_length is not None and len(self.vertices) >= max_length:
            # cannot add more points!
            raise ValueError(f'Vertices length is at max ({max_length})')
        self.vertices.append(pt)

    def __len__(self):
        return len(self.vertices)

    def __getitem__(self, idx):
        return self.vertices[idx]

    def __iadd__(self, pt):
        self.append(pt)
        return self

    def __contains__(self, pt):
        return pt in self.vertices

p = Polygon(Point2D(0, 0), Point2D(1, 0), Point2D(1, 1))
print(f'list(p) = {list(p)}')
p += Point2D(10, 10)
print(f'list(p) = {list(p)}')
print(f'Point2D(0, 0) in p = {Point2D(0, 0) in p}')

line_break()

class Point2D:
    x = Int(min_value=0, max_value=800)
    y = Int(min_value=0, max_value=400)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point2D(x={self.x}, y={self.y})'

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __eq__(self, other):
        return isinstance(other, Point2D) and self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

class Polygon:
    vertices = Point2DSequence(min_length=3)

    def __init__(self, *vertices):
        self.vertices = vertices

    def append(self, pt):
        if not isinstance(pt, Point2D):
            raise ValueError('Can only append Point2D instances.')
        max_length = type(self).vertices.max_length
        if max_length is not None and len(self.vertices) >= max_length:
            # cannot add more points!
            raise ValueError(f'Vertices length is at max ({max_length})')
        self.vertices.append(pt)

    def __len__(self):
        return len(self.vertices)

    def __getitem__(self, idx):
        return self.vertices[idx]

    def __iadd__(self, pt):
        self.append(pt)
        return self

    def __contains__(self, pt):
        return pt in self.vertices

p = Polygon(Point2D(0, 0), Point2D(1, 0), Point2D(1, 1))
print(f'list(p) = {list(p)}')
p += Point2D(10, 10)
print(f'list(p) = {list(p)}')
print(f'Point2D(0, 0) in p = {Point2D(0, 0) in p}')