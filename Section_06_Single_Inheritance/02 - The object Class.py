def line_break():
    x = 0
    print("\n\n")
    while x < 20:
        print("*", end="")
        x += 1
    print("\n\n")

line_break()

print("type(object): " + str(type(object)))
print("type(int), type(str), type(dict): " + str(type(int)), str(type(str)), str(type(dict)))

line_break()

class Person:
    pass

print("issubclass(Person, object): " + str(issubclass(Person, object)))
print("issubclass(int, object): " + str(issubclass(int, object)))

line_break()

import math

print(f"type(math): {type(math)}")

ty = type(math)
print(f"type(ty): {type(ty)}")
print(f"issubclass(ty, object): {issubclass(ty, object)}")

line_break()

import types
print(f"dir(types): {dir(types)}")

def my_func():
    pass

print(f"type(my_func): {type(my_func)}")
print(f"types.FunctionType is type(my_func): {types.FunctionType is type(my_func)}")
print(f"issubclass(types.FunctionType, object): {issubclass(types.FunctionType, object)}")
print(f"isinstance(my_func, object): {isinstance(my_func, object)}")
print(f"isinstance(my_func, types.FunctionType): {isinstance(my_func, types.FunctionType)}")

line_break()

print(f"dir(object): {dir(object)}")
o1 = object()
print(f"str(o1): {str(o1)}")
print(f"repr(o1): {repr(o1)}")

class Person:
    pass
p = Person()
print(f"str(p): {str(p)}")

o1 = object()
o2 = object()

print(f"id(o1), id(o2): {id(o1)}, {id(o2)}")
print(f"o1 is o2, o1 == o2, o1 is o1, o1 == o1: {o1 is o2}, {o1 == o2}, {o1 is o1}, {o1 == o1}")

p1 = Person()
p2 = Person()

print(f"p1 is p2, p1 == p2, p1 is p1, p1 == p1: {p1 is p2}, {p1 == p2}, {p1 is p1}, {p1 == p1}")
print(f"id(Person.__eq__): {id(Person.__eq__)}")
print(f"id(object.__eq__): {id(object.__eq__)}")
print(f"id(Person.__init__), id(object.__init__): {id(Person.__init__)}, {id(object.__init__)}")

class Person:
    def __init__(self):
        pass


print(f"id(Person.__init__), id(object.__init__): {id(Person.__init__)}, {id(object.__init__)}")