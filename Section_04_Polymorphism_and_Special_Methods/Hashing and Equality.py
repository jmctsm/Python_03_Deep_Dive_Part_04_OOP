def line_break():
    x = 0
    print("\n\n")
    while x < 20:
        print("*", end="")
        x += 1
    print("\n\n")


line_break()

print(dir(object))

line_break()

class Person:
    pass

p1 = Person()
p2 = Person()

print(hash(p1), hash(p2))
print(p1 == p2)

line_break()

class Person:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        print('__eq__ called...')
        return isinstance(other, Person) and self.name == other.name

p1 = Person('John')
p2 = Person('John')
p3 = Person('Eric')

print(p1 == p2, p1 == p3)
try:
    print(hash(p1))
except TypeError as ex:
    print(ex)
print(type(p1.__hash__))
try:
    d = {p1: 'Person 1'}
except TypeError as ex:
    print(ex)

line_break()

class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def __eq__(self, other):
        print('__eq__ called...')
        return isinstance(other, Person) and self.name == other.name

    def __hash__(self):
        print('__hash__ called...')
        return hash(self.name)

p1 = Person('Eric')
d = {p1: 'Eric'}
print(d)
s = {p1}
