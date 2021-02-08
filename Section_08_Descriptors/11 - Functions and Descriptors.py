def line_break():
    x = 0
    print("\n\n")
    while x < 20:
        print("*", end="")
        x += 1
    print("\n\n")


line_break()

def add(a, b):
    return a + b

print(f"hasattr(add, '__get__') = {hasattr(add, '__get__')}")

line_break()

import sys

me = sys.modules['__main__']

p = add.__get__(None, me)
print(f"p , id(p) = {p, id(p)}")
print(f"add , id(add) = {add, id(add)}")

line_break()

class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        return f'{self.name} says hello'

print(f"Person.say_hello = {Person.say_hello}")

p = Person('Alex')
print(f'hex(id(p)) = {hex(id(p))}')

print(f'p.say_hello = {p.say_hello}')

bound_method = Person.say_hello.__get__(p, Person)
print(f'bound_method = {bound_method}')
print(f'p.say_hello() = {p.say_hello()}')
print(f'bound_method() = {bound_method()}')

print(f'p.say_hello.__func__, id(p.say_hello.__func__ = {p.say_hello.__func__, id(p.say_hello.__func__)}')

print(f'p.say_hello.__func__ is Person.say_hello = {p.say_hello.__func__ is Person.say_hello}')

line_break()


class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        return f'{self.name} says hallo!'

def say_hello(self):
    if self and hasattr(self, 'name'):
        return f'{self.name} says hello!'
    else:
        return 'Hello!'

print(f'say_hello(None) = {say_hello(None)}')

line_break()

import types

print(help(types.MethodType))

line_break()

class Person:
    def __init__(self, name):
        self.name = name

p = Person('Alex')
m = types.MethodType(say_hello, p)
print(f'p , m = {p , m}')

print(f'm() = {m()}')

class MyFunc:
    def __init__(self, func):
        self._func = func

    def __get__(self, instance, owner):
        if instance is None:
            # called from class
            print('__get__ called from class')
            return self._func
        else:
            # called from an instance
            print("__get__ called from an instance")
            return types.MethodType(self._func, instance)

def hello(self):
    print(f'{self.name} says hello!')

class Person:
    def __init__(self, name):
        self.name = name

    say_hello = MyFunc(hello)

print(f'Person.say_hello = {Person.say_hello}')

p = Person('Alex')
print(f'p.say_hello = {p.say_hello}')
print(f'p.say_hello() = {p.say_hello()}')

print(f'p.say_hello.__func__ = {p.say_hello.__func__}')