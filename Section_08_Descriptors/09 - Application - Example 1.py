def line_break():
    x = 0
    print("\n\n")
    while x < 20:
        print("*", end="")
        x += 1
    print("\n\n")


line_break()

class Int:
    def __set_name__(self, owner_class, prop_name):
        self.prop_name = prop_name

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError(f'{self.prop_name} must be an integer')
        instance.__dict__[self.prop_name] = value

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return instance.__dict__.get(self.prop_name, None)

class Float:
    def __set_name__(self, owner_class, prop_name):
        self.prop_name = prop_name

    def __set__(self, instance, value):
        if not isinstance(value, float):
            raise ValueError(f'{self.prop_name} must be an float')
        instance.__dict__[self.prop_name] = value

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return instance.__dict__.get(self.prop_name, None)

class List:
    def __set_name__(self, owner_class, prop_name):
        self.prop_name = prop_name

    def __set__(self, instance, value):
        if not isinstance(value, list):
            raise ValueError(f'{self.prop_name} must be a list')
        instance.__dict__[self.prop_name] = value

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return instance.__dict__.get(self.prop_name, None)

class Person:
    age = Int()
    height = Float()
    tags = List()
    favorite_foods = List()

p = Person()
try:
    p.age = 12.5
except ValueError as ex:
    print(ex)
try:
    p.height = 'abc'
except ValueError as ex:
    print(ex)
try:
    p.tags = 'python'
except ValueError as ex:
    print(ex)

line_break()

class ValidType:
    def __init__(self, type_):
        self._type = type_

    def __set_name__(self, owner_class, prop_name):
        self.prop_name = prop_name

    def __set__(self, instance, value):
        if not isinstance(value, self._type):
            raise ValueError(f'{self.prop_name} must be of type {self._type.__name__}')
        instance.__dict__[self.prop_name] = value

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return instance.__dict__.get(self.prop_name, None)

class Person:
    age = ValidType(int)
    height = ValidType(float)
    tags = ValidType(list)
    favorite_foods = ValidType(tuple)
    name = ValidType(str)

p = Person()
try:
    p.age = 12.5
except ValueError as ex:
    print(ex)
try:
    p.height = 10
except ValueError as ex:
    print(ex)

line_break()

import numbers

print(f'isinstance(10.1, numbers.Real) = {isinstance(10.1, numbers.Real)}')
print(f'isinstance(10, numbers.Real) = {isinstance(10, numbers.Real)}')

class Person:
    age = ValidType(int)
    height = ValidType(numbers.Real)
    tags = ValidType(list)
    favorite_foods = ValidType(tuple)
    name = ValidType(str)

p = Person()
p.height = 10

print(f'p.height = {p.height}')
