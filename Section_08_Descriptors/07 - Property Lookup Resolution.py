def line_break():
    x = 0
    print("\n\n")
    while x < 20:
        print("*", end="")
        x += 1
    print("\n\n")


line_break()


class IntegerValue:
    def __set__(self, instance, value):
        print("__set__ called...")

    def __get__(self, instance, owner_class):
        print("__get__ called")

class Point:
    x = IntegerValue()

p = Point()

p.x = 100

print(f'p.x = {p.x}')

print(f'p.__dict__ = {p.__dict__}')

p.__dict__['x'] = 'hello'

print(f'p.__dict__ = {p.__dict__}')

print(f'p.x = {p.x}')

p.x = 100

line_break()

from datetime import datetime

class TimeUTC:
    def __get__(self, instance, owner_class):
        print('__get__ called...')
        return datetime.utcnow().isoformat()

class Logger:
    current_time = TimeUTC()

l = Logger()

print(f'l.current_time = {l.current_time}')

print(f'l.__dict__ = {l.__dict__}')

l.__dict__['current_time'] = 'This is not a timestamp'
print(f'l.__dict__ = {l.__dict__}')
print(f'l.current_time = {l.current_time}')

del l.__dict__['current_time']
print(f'l.__dict__ = {l.__dict__}')
print(f'l.current_time = {l.current_time}')

line_break()

class ValidString:
    def __init__(self, min_length):
        self.min_length = min_length

    def __set_name__(self, owner_class, prop_name):
        self.prop_name = prop_name

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f'{self.prop_name} must be a string')
        if len(value) < self.min_length:
            raise ValueError(f'{self.prop_name} must be at least {self.min_length} characters.')
        instance.__dict__[self.prop_name] = value

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return instance.__dict__.get(self.prop_name, None)

class Person:
    first_name = ValidString(1)
    last_name = ValidString(2)

p = Person()

print(f'p.__dict__ = {p.__dict__}')
p.first_name = 'Alex'
p.last_name = 'Martelli'
print(f'p.__dict__ = {p.__dict__}')
print(f'p.first_name , p.last_name = {p.first_name} , {p.last_name}')

line_break()

class ValidString:
    def __init__(self, min_length):
        self.min_length = min_length

    def __set_name__(self, owner_class, prop_name):
        self.prop_name = prop_name

    def __set__(self, instance, value):
        print('Calling __set__...')
        if not isinstance(value, str):
            raise ValueError(f'{self.prop_name} must be a string')
        if len(value) < self.min_length:
            raise ValueError(f'{self.prop_name} must be at least {self.min_length} characters.')
        setattr(instance, self.prop_name, value)

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return instance.__dict__.get(self.prop_name, None)

class Person:
    name = ValidString(1)

p = Person()
p.name = 'Alex'

