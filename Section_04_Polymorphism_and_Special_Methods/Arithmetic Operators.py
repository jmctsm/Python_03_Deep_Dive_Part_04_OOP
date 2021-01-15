def line_break():
    x = 0
    print("\n\n")
    while x < 20:
        print("*", end="")
        x += 1
    print("\n\n")


line_break()

from numbers import Real
from math import sqrt

class Vector:
    def __init__(self, *components):
        # validate number of components is at least one, and all of them are real numbers
        if len(components) < 1:
            raise ValueError('Cannot create an empty Vector')
        for component in components:
            if not isinstance(component, Real):
                raise ValueError(f'Vector components must all be real numbers - {component} is invalid')

        # use immutable storage for vector
        self._components = tuple(components)

    def __len__(self):
        return len(self._components)

    @property
    def components(self):
        return self._components

    def validate_type_and_dimension(self, v):
        return isinstance(v, Vector) and len(v) == len(self)

    def __add__(self, other):
        if not self.validate_type_and_dimension(other):
            return NotImplemented
        components = (x + y for x, y in zip(self._components, other.components))
        return Vector(*components)

    def __sub__(self, other):
        if not self.validate_type_and_dimension(other):
            return NotImplemented
        components = (x - y for x, y in zip(self._components, other.components))
        return Vector(*components)

    def __repr__(self):
        # works - but unwieldly for high dimension vectors
        return f'Vector{self._components}'

    def __mul__(self, other):
        print('__mul__ called...')
        if isinstance(other, Real):
            components = (other * x for x in self.components)
            return Vector(*components)
        if self.validate_type_and_dimension(other):
            # dot product
            components = (x * y for x, y in zip(self.components, other.components))
            return sum(components)
        return NotImplemented

    def __rmul__(self, other):
        print('__rmul__ called')
        # for us, multiplication is commutative, so we can leverage our existing __mul__ method
        return self * other

    def __matmul__(self, other):
        print('__matmul__ called ...')

v1 = Vector(1, 2)
v2 = Vector(10, 10)
v3 = Vector(1, 2, 3, 4)

print(v1)
print(v1 + v2)
print(v2 + v1)

try:
    print(v1 + v3)
except TypeError as ex:
    print(ex)

try:
    print(v1 + 100)
except TypeError as ex:
    print(ex)

print(v1 * 10)

try:
    print(10 * v1)
except TypeError as ex:
    print(ex)

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 * v2)
print(v1 @ v2)

line_break()

class Vector:
    def __init__(self, *components):
        # validate number of components is at least one, and all of them are real numbers
        if len(components) < 1:
            raise ValueError('Cannot create an empty Vector')
        for component in components:
            if not isinstance(component, Real):
                raise ValueError(f'Vector components must all be real numbers - {component} is invalid')

        # use immutable storage for vector
        self._components = tuple(components)

    def __len__(self):
        return len(self._components)

    @property
    def components(self):
        return self._components

    def validate_type_and_dimension(self, v):
        return isinstance(v, Vector) and len(v) == len(self)

    def __add__(self, other):
        if not self.validate_type_and_dimension(other):
            return NotImplemented
        components = (x + y for x, y in zip(self._components, other.components))
        return Vector(*components)

    def __sub__(self, other):
        if not self.validate_type_and_dimension(other):
            return NotImplemented
        components = (x - y for x, y in zip(self._components, other.components))
        return Vector(*components)

    def __repr__(self):
        # works - but unwieldly for high dimension vectors
        return f'Vector{self._components}'

    def __mul__(self, other):
        print('__mul__ called...')
        if isinstance(other, Real):
            components = (other * x for x in self.components)
            return Vector(*components)
        if self.validate_type_and_dimension(other):
            # dot product
            components = (x * y for x, y in zip(self.components, other.components))
            return sum(components)
        return NotImplemented

    def __rmul__(self, other):
        print('__rmul__ called')
        # for us, multiplication is commutative, so we can leverage our existing __mul__ method
        return self * other

    def __matmul__(self, other):
        print('__matmul__ called ...')

    def __iadd__(self, other):
        print("__radd__ called...")
        if self.validate_type_and_dimension(other):
            components = (x + y for x, y in zip(self.components, other.components))
            self._components = tuple(components) # mutating our vector object
            return self # don't forget to return the result of the operation
        return NotImplemented

    def __neg__(self):
        print("__neg__ called...")
        components = (-x for x in self.components)
        return Vector(*components)

    def __abs__(self):
        print("__abs__ called...")
        return sqrt(sum(x  ** 2 for x in self.components))

v1 = Vector(1,2)
v2 = Vector(10, 10)
print(id(v1))
v1 += v2
print(id(v1), v1)
v1 = Vector(1,2)
v2 = Vector(10, 20)
print(id(v1))
v1 += v2
print(id(v1), v1)

v1 = Vector(1,2)
print(-v1)
v2 = Vector(10, 10)
print(v2 + -v1)

v1 = Vector(1, 1)
print(abs(v1))

line_break()

class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Person('{self.name}')"

p1 = Person('John')

class Family:
    def __init__(self, mother, father):
        self.mother = mother
        self.father = father
        self.children = []

    def __iadd__(self, other):
        self.children.append(other)
        return self

f = Family(Person('Mary'), Person('John'))
print(id(f))

f += Person('Eric')
print(id(f))
print(f.children)

f += Person('Michael')
print(id(f))
print(f.children)