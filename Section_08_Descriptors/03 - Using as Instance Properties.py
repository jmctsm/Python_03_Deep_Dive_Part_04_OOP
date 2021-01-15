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
        instance.stored_value = int(value)

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return getattr(instance, 'stored_value', None)

class Point1D:
    x = IntegerValue()

p1, p2 = Point1D(), Point1D()

p1.x = 10.1
p2.x = 20.2
print(f'p1.x , p2.x = {p1.x} , {p2.x}')
print(f'p1.__dict__ , p2.__dict__ = {p1.__dict__} , {p2.__dict__}')

class Point2D:
    x = IntegerValue()
    y = IntegerValue()

p = Point2D()
p.x = 10.1
print(f'p.__dict__ = {p.__dict__}')
p.y = 20.2
print(f'p.__dict__ = {p.__dict__}')
print(f'p.x , p.y = {p.x} , {p.y}')

line_break()

class IntegerValue:
    def __init__(self, name):
        self.storage_name = '_' + name

    def __set__(self, instance, value):
        setattr(instance, self.storage_name, int(value))

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return getattr(instance, self.storage_name, None)

class Point2D:
    x = IntegerValue('x')
    y = IntegerValue('y')

p1 = Point2D()
p2 = Point2D()

p1.x = 10.1
p1.y = 20.2
print(f'p1.__dict__ = {p1.__dict__}')
p2.x = 100.1
p2.y = 200.2
print(f'p2.__dict__ = {p2.__dict__}')
print(f'p1.__dict__ = {p1.__dict__}')

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


class Point2D:
    x = IntegerValue()
    y = IntegerValue()

p1 = Point2D()
p2 = Point2D()

p1.x = 10.1
p1.y = 20.2
print(f'p1.x , p1.y = {p1.x} , {p1.y}')

print(f'Point2D.x.values = {Point2D.x.values}')
print(f'Point2D.y.values = {Point2D.y.values}')
print(f'hex(id(p1)) = {hex(id(p1))}')

p2.x = 100.1
p2.y = 200.2
print(f'p2.x , p2.y = {p2.x} , {p2.y}')

print(f'Point2D.x.values = {Point2D.x.values}')
print(f'Point2D.y.values = {Point2D.y.values}')
print(f'hex(id(p2)) = {hex(id(p2))}')

print(f'p1.x , p1.y , p2.x , p2.y = {p1.x} , {p1.y} , {p2.x} , {p2.y}')

line_break()

import ctypes

def ref_count(address):
    return ctypes.c_long.from_address(address).value

p1 = Point2D()
id_p1 = id(p1)

print(f'ref_count(id_p1) = {ref_count(id_p1)}')

p1.x = 100.1
print(f'ref_count(id_p1) = {ref_count(id_p1)}')
print(f"'p1' in globals() = {'p1' in globals()}")
del p1
print(f"'p1' in globals() = {'p1' in globals()}")
print(f'ref_count(id_p1) = {ref_count(id_p1)}')
print(f'Point2D.x.values = {Point2D.x.values}')
print(f'hex(id_p1) = {hex(id_p1)}')