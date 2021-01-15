def line_break():
    x = 0
    print("\n\n")
    while x < 20:
        print("*", end="")
        x += 1
    print("\n\n")

line_break()

class Person:
    def work(self):
        return 'Person works...'

class Student(Person):
    def work(self):
        result = super().work()
        return f'Student works... and {result}'

s = Student()
print(f"s.work(): {s.work()}")

line_break()

class Person:
    def work(self):
        return 'Person works...'

class Student(Person):
    pass

class PythonStudent(Student):
    def work(self):
        result = super().work()
        return f'PythonStudent codes... and {result}'

ps = PythonStudent()
print(f"ps.work(): {ps.work()}")

line_break()

class Person:
    def work(self):
        return 'Person works...'

class Student(Person):
    def work(self):
        result = super().work()
        return f'Student studies... and {result}'

class PythonStudent(Student):
    def work(self):
        result = super().work()
        return f'PythonStudent codes... and {result}'

ps = PythonStudent()
print(f"ps.work(): {ps.work()}")

line_break()

class Person:
    def work(self):
        return 'Person works...'

class Student(Person):
    def study(self):
        return 'Student studies...'

class PythonStudent(Student):
    def code(self):
        result_1 = self.work()
        result_2 = self.study()
        return f'{result_1} and {result_2} and PythonStudent codes...'

ps = PythonStudent()
print(f"ps.code(): {ps.code()}")

line_break()

class Person:
    def work(self):
        return f'{self} works...'

class Student(Person):
    def work(self):
        result = super().work()
        return f'{self} studies... and {result}'

class PythonStudent(Student):
    def work(self):
        result = super().work()
        return f'{self} codes... and {result}'

ps = PythonStudent()
print(f'hex(id(ps)) = {hex(id(ps))}')
print(f'ps.work(): {ps.work()}')

line_break()

class Person:
    def set_name(self, value):
        print('Setting name using Person set_name method...')
        self.name = value

class Student(Person):
    def set_name(self, value):
        print('Student class delegating back to parent...')
        super().set_name(value)

s = Student()
print(f's.__dict__: {s.__dict__}')
s.set_name('Eric')
print(f's.__dict__: {s.__dict__}')

line_break()

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, student_number):
        super().__init__(name)
        self.student_number = student_number

s = Student('Python', 30)
print(f's.__dict__: {s.__dict__}')

line_break()

class Person:
    def __init__(self):
        print('Person __init__')

class Student(Person):
    pass

s = Student()

line_break()

class Person:
    def __init__(self, name):
        print('Person __init__')
        self.name = name

class Student(Person):
    pass

try:
    s = Student()
except TypeError as ex:
    print(ex)
s = Student('Alex')
print(f's.__dict__ = {s.__dict__}')

line_break()

class Person:
    def __init__(self):
        print('Person __init__ called...')

class Student(Person):
    def __init__(self):
        print('Student __init__ called...')

s = Student()

line_break()

class Person:
    def __init__(self):
        print('Person __init__ called...')

class Student(Person):
    def __init__(self):
        super().__init__()
        print('Student __init__ called...')

s = Student()

line_break()

from math import pi
from numbers import Real

class Circle:
    def __init__(self, r):
        self._r = r
        self._area = None
        self._perimeter = None

    @property
    def radius(self):
        return self._r

    @radius.setter
    def radius(self, r):
        if isinstance(r, Real) and r > 0:
            self._r = r
            self._area = None
            self._perimeter = None
        else:
            raise ValueError('Radius must be a positive number.')

    @property
    def area(self):
        if self._area is None:
            self._area = pi * self.radius ** 2
        return self._area

    @property
    def perimeter(self):
        if self._perimeter is None:
            self._perimeter = 2 * pi * self.radius
        return self._perimeter

class UnitCircle(Circle):
    def __init__(self):
        super().__init__(1)

u = UnitCircle()
print(f'u.radius, u.area, u.perimeter = {u.radius}, {u.area}, {u.perimeter}')

line_break()

class Circle:
    def __init__(self, r):
        self._r = r
        self._area = None
        self._perimeter = None

    @property
    def radius(self):
        return self._r

    @radius.setter
    def radius(self, r):
        if isinstance(r, Real) and r > 0:
            self._r = r
            self._area = None
            self._perimeter = None
        else:
            raise ValueError('Radius must be a positive number.')

    @property
    def area(self):
        if self._area is None:
            self._area = pi * self.radius ** 2
        return self._area

    @property
    def perimeter(self):
        if self._perimeter is None:
            self._perimeter = 2 * pi * self.radius
        return self._perimeter

class UnitCircle(Circle):
    def __init__(self):
        super().__init__(1)

    @property
    def radius(self):
        return super().radius

u = UnitCircle()
print(f'u.radius, u.area, u.perimeter = {u.radius}, {u.area}, {u.perimeter}')
try:
    u.radius = 10
except AttributeError as ex:
    print(ex)

line_break()

class Person:
    def method_1(self):
        print('Person.method_1')
        self.method_2()

    def method_2(self):
        print('Person.method_2')

class Student(Person):
    def method_1(self):
        print('Student.method_1')
        super().method_1()

s = Student()
s.method_1()

line_break()

class Person:
    def method_1(self):
        print('Person.method_1')
        self.method_2()

    def method_2(self):
        print('Person.method_2')

class Student(Person):
    def method_1(self):
        print('Student.method_1')
        super().method_1()

    def method_2(self):
        print('Student.method_2')

s = Student()
s.method_1()
