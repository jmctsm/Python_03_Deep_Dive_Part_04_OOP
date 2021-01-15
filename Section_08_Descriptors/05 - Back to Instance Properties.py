def line_break():
    x = 0
    print("\n\n")
    while x < 20:
        print("*", end="")
        x += 1
    print("\n\n")


line_break()

import weakref
import ctypes

line_break()

class IntegerValue:
    def __init__(self):
        self.values = {}

    def __set__(self, instance, value):
        self.values[instance] = int(value)

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return self.values.get(instance)

line_break()

class IntegerValue:
    def __init__(self):
        self.values = weakref.WeakKeyDictionary()

    def __set__(self, instance, value):
        self.values[instance] = int(value)

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return self.values.get(instance)

class Point:
    x = IntegerValue()

p = Point()
print(f'hex(id(p)) = {hex(id(p))}')
p.x = 100.1
print(f'p.x = {p.x}')
print(f'Point.x.values.keyrefs() = {Point.x.values.keyrefs()}')

del p
print(f'Point.x.values.keyrefs() = {Point.x.values.keyrefs()}')

line_break()

class IntegerValue:
    def __init__(self):
        self.values = {}

    def __set__(self, instance, value):
        self.values[id(instance)] = int(value)

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return self.values.get(id(instance))

class Point:
    x = IntegerValue()

    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x

p = Point(10.1)
print(f'p.x = {p.x}')
p.x = 20.2
print(f'p.x = {p.x}')
print(f'id(p) , Point.x.values = {id(p)} , {Point.x.values}')

def ref_count(address):
    return ctypes.c_long.from_address(address).value

p_id = id(p)
print(f'ref_count(p_id) = {ref_count(p_id)}')
del p
print(f'ref_count(p_id) = {ref_count(p_id)}')
print(f'Point.x.values = {Point.x.values}')
