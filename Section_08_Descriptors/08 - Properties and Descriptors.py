def line_break():
    x = 0
    print("\n\n")
    while x < 20:
        print("*", end="")
        x += 1
    print("\n\n")


line_break()

from numbers import Integral

class Person:
    @property
    def age(self):
        return getattr(self, '_age', None)

    @age.setter
    def age(self, value):
        if not isinstance(value, Integral):
            raise ValueError('age: must be an integer')
        if value < 0:
            raise ValueError('age: must be a non-negative integer.')
        self._age = value

p = Person()

try:
    p.age = -10
except ValueError as ex:
    print(ex)

p.age = 10

print(f'p.age , p.__dict__ = {p.age} , {p.__dict__}')

line_break()

class Person:
    def get_age(self):
        return getattr(self, '_age', None)

    def set_age(self, value):
        if not isinstance(value, Integral):
            raise ValueError('age: must be an integer')
        if value < 0:
            raise ValueError('age: must be a non-negative integer.')
        self._age = value

    age = property(fget=get_age, fset=set_age)

p = Person()

try:
    p.age = -10
except ValueError as ex:
    print(ex)

p.age = 10

print(f'p.age , p.__dict__ = {p.age} , {p.__dict__}')

prop = Person.age
print(f'prop = {prop}')
print(f"hasattr(prop, '__set__') = {hasattr(prop, '__set__')}")
print(f"hasattr(prop, '__get__') = {hasattr(prop, '__get__')}")

line_break()

from datetime import datetime

class TimeUTC:
    @property
    def current_time(self):
        return datetime.utcnow().isoformat()

t = TimeUTC()
print(f't.current_time = {t.current_time}')

prop = TimeUTC.current_time
print(f'prop = {prop}')
print(f"hasattr(prop, '__set__') = {hasattr(prop, '__set__')}")
print(f"hasattr(prop, '__get__') = {hasattr(prop, '__get__')}")

try:
    t.current_time = datetime.utcnow().isoformat()
except AttributeError as ex:
    print(ex)

print(f't.__dict__ = {t.__dict__}')
t.__dict__['current_time'] = 'not a time'
print(f't.__dict__ = {t.__dict__}')
print(f't.current_time = {t.current_time}')

line_break()

class MakeProperty:
    def __init__(self, fget=None, fset=None):
        self.fget = fget
        self.fset = fset

    def __set_name__(self, owner_class, prop_name):
        self.prop_name = prop_name

    def __get__(self, instance, owner_class):
        print('__get__ called...')
        if instance is None:
            return self
        if self.fget is None:
            raise AttributeError(f'{self.prop_name} is not readable')
        return self.fget(instance)

    def __set__(self, instance, value):
        print('__set__ called...')
        if self.fset is None:
            raise AttributeError(f'{self.prop_name} is not writable')
        self.fset(instance, value)

class Person:
    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    name = MakeProperty(fget=get_name, fset=set_name)

p = Person()
print(f'p.__dict__ = {p.__dict__}')
p.name = 'Guido'
print(f'p.name = {p.name}')

p.__dict__['name'] = 'Alex'
print(f'p.__dict__ = {p.__dict__}')
print(f'p.name = {p.name}')

line_break()

class MakeProperty:
    def __init__(self, fget=None, fset=None):
        self.fget = fget
        self.fset = fset

    def __set_name__(self, owner_class, prop_name):
        self.prop_name = prop_name

    def __get__(self, instance, owner_class):
        print('__get__ called...')
        if instance is None:
            return self
        if self.fget is None:
            raise AttributeError(f'{self.prop_name} is not readable')
        return self.fget(instance)

    def __set__(self, instance, value):
        print('__set__ called...')
        if self.fset is None:
            raise AttributeError(f'{self.prop_name} is not writable')
        self.fset(instance, value)

    def setter(self, fset):
        self.fset = fset
        return self

class Person:
    def get_first_name(self):
        return getattr(self, '_first_name', None)

    def set_first_name(self, value):
        self._first_name = value

    def get_last_name(self):
        return getattr(self, '_last_name', None)

    def set_last_name(self, value):
        self._last_name = value

    first_name = MakeProperty(fset=get_first_name, fget=set_first_name)
    last_name = MakeProperty(fset=get_last_name, fget=set_last_name)

class Person:
    @MakeProperty
    def first_name(self):
        return getattr(self, '_first_name', None)

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @MakeProperty
    def last_name(self):
        return getattr(self, '_last_name', None)

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

p1 = Person()
p1.first_name = "Raymond"
p1.last_name = 'Hettinger'

print(f'p1.first_name = {p1.first_name}')
print(f'p1.last_name = {p1.last_name}')

p2 = Person()
p2.first_name, p2.last_name = 'Alex', 'Martelli'

print(f'p1.first_name , p1.last_name , p2.first_name , p2.last_name = '
      f'{p1.first_name} , {p1.last_name} , {p2.first_name} , {p2.last_name}')