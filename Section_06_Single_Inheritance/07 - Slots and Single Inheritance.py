def line_break():
    x = 0
    print("\n\n")
    while x < 20:
        print("*", end="")
        x += 1
    print("\n\n")

line_break()

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    pass

s = Student('Alex')
print(f's.__dict__ = {s.__dict__}')

line_break()

class Person:
    __slots__ = 'name',

    def __init__(self, name):
        self.name = name

class Student(Person):
    pass

p = Person('Eric')

try:
    print(f'p.__dict__ = {p.__dict__}')
except AttributeError as ex:
    print(f'AttributeError = {ex}')

s = Student('Alex')
print(f's.name, s.__dict__ = {s.name} , {s.__dict__}')
s.age = 19
print(f's.__dict__ = {s.__dict__}')
print(f's.name, s.age = {s.name} , {s.age}')

line_break()
class Student(Person):
    __slots__ = tuple()

s = Student('Alex')
print(f's.name = {s.name}')

try:
    print(f's.__dict__ = {s.__dict__}')
except AttributeError as ex:
    print(f'AttributeError = {ex}')

line_break()

class Student(Person):
    __slots__ = 'school', 'student_number'

    def __init__(self, name, school, student_number):
        super().__init__(name)
        self.school = school
        self.student_number = student_number

s = Student('James', 'MI6 Prep School', '007')

print(f's.name, s.school, s.student_number = {s.name}, {s.school}, {s.student_number}')

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    __slots__ = 'age',

    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

s = Student('Python', 30)
print(f's.name, s.age, s.__dict__ = {s.name}, {s.age}, {s.__dict__}')

line_break()

class Person:
    __slots__ = '_name', 'age'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

p = Person('Eric', 78)

print(f'p.name, p.age = {p.name}, {p.age}')

try:
    print(f'p.__dict__ = {p.__dict__}')
except AttributeError as ex:
    print(f'AttributeError = {ex}')

line_break()

print(f"hasattr(Person.name, '__get__'), hasattr(Person.name, '__set__') = {hasattr(Person.name, '__get__')}, {hasattr(Person.name, '__set__')}")

print(f"hasattr(Person.age, '__get__'), hasattr(Person.age, '__set__') = {hasattr(Person.age, '__get__')}, {hasattr(Person.age, '__set__')}")

line_break()

class Person:
    __slots__ = 'name', '__dict__'

    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person('Alex', 19)
print(f'p.name, p.age, p.__dict__ = {p.name}, {p.age}, {p.__dict__}')
p.school = "Berkeley"
print(f'p.name, p.age, p.__dict__ = {p.name}, {p.age}, {p.__dict__}')
