def line_break():
    x = 0
    print("\n\n")
    while x < 20:
        print("*", end="")
        x += 1
    print("\n\n")


line_break()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        print('__repr__ called')
        return f"Person(name='{self.name}, age={self.age}')"


p = Person('Python', 30)
print(p)
print(repr(p))
print(str(p))

line_break()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        print('__repr__ called')
        return f"Person(name='{self.name}, age={self.age}')"

    def __str__(self):
        print('__str__ called')
        return self.name


p = Person('Python', 30)
print(p)
print(str(p))
print(repr(p))

line_break()

class Person:
    pass

class Point:
    pass

person = Person()
point = Point()

print(repr(person), repr(point))
print(str(person), str(point))

line_break()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        print('__str__ called')
        return self.name


p = Person('Python', 30)

print(p)
print(str(p))
print(repr(p))


line_break()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        print('__repr__ called')
        return f"Person(name='{self.name}, age=self.age')"

    def __str__(self):
        print('__str__ called')
        return self.name

p = Person('Python', 30)
print(f'The person is {p}')
print('The person is {}'.format(p))
print('The person is %s' % p)
