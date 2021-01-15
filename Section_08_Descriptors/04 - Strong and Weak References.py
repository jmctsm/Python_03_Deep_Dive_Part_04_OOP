def line_break():
    x = 0
    print("\n\n")
    while x < 20:
        print("*", end="")
        x += 1
    print("\n\n")

line_break()

import ctypes


def ref_count(address):
    return ctypes.c_long.from_address(address).value


class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Person(name={self.name})'

p1 = Person('Guido')
p2 = p1

p1_id = id(p1)
p2_id = id(p2)

print(f'p1_id == p2_id , ref_count(p1_id) = {p1_id == p2_id} , {ref_count(p1_id)}')

del p2

print(f'ref_count(p1_id) = {ref_count(p1_id)}')

del p1

print(f'ref_count(p1_id) = {ref_count(p1_id)}')

line_break()

import weakref

p1 = Person('Kelly')
p1_id = id(p1)
print(f'ref_count(p1_id) = {ref_count(p1_id)}')
p2 = p1
print(f'ref_count(p1_id) = {ref_count(p1_id)}')
weak1 = weakref.ref(p1)
print(f'ref_count(p1_id) = {ref_count(p1_id)}')

print(f'weak1 = {weak1}')
print(f'hex(p1_id) = {hex(p1_id)}')
print(f'weak1 is p1 = {weak1 is p1}')
print(f'ref_count(p1_id) = {ref_count(p1_id)}')
print(f'weak1() is p1 = {weak1() is p1}')
print(f'weak1() = {weak1()}')
print(f'ref_count(p1_id) = {ref_count(p1_id)}')
p3 = weak1()
print(f'p1 is p3 = {p1 is p3}')
print(f'ref_count(p1_id) = {ref_count(p1_id)}')
print(f'weakref.getweakredcount(p1) , ref_count(p1_id) = {weakref.getweakrefcount(p1)} , {ref_count(p1_id)}')

import sys
print(f'sys.getrefcount(p1) = {sys.getrefcount(p1)}')

del p3
del p2
print(f'ref_count(p1_id) = {ref_count(p1_id)}')

del p1
print(f'weak1 = {weak1}')

obj = weak1()
print(f'obj is None = {obj is None}')

line_break()

l = [1, 2, 3]
try:
    w = weakref.ref(l)
except TypeError as ex:
    print(ex)

l = {'a': 1}
try:
    w = weakref.ref(l)
except TypeError as ex:
    print(ex)

l = 100
try:
    w = weakref.ref(l)
except TypeError as ex:
    print(ex)

l = 'Python'
try:
    w = weakref.ref(l)
except TypeError as ex:
    print(ex)

line_break()

p1 = Person('Guido')
d = weakref.WeakKeyDictionary()
print(f'ref_count(id(p1)) = {ref_count(id(p1))}')
print(f'weakref.getweakrefcount(p1) = {weakref.getweakrefcount(p1)}')
d[p1] = 'Guido'
print(f'ref_count(id(p1)) = {ref_count(id(p1))}')
print(f'weakref.getweakrefcount(p1) = {weakref.getweakrefcount(p1)}')
print(f'hex(id(p1)) , list(d.keyrefs()) = {hex(id(p1))} , {list(d.keyrefs())}')
del p1
print(f'list(d.keyrefs()) = {list(d.keyrefs())}')

line_break()

try:
    d['Python'] = 'test'
except TypeError as ex:
    print(ex)

line_break()

class Person:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return isinstance(other, Person) and self.name == self.name

p1 = Person('Guido')
p2 = Person('Guido')

print(f'p1 == p2 = {p1 == p2}')

try:
    hash(p1)
except TypeError as ex:
    print(ex)

try:
    d[p1] = 'Guido'
except TypeError as ex:
    print(ex)
