def line_break():
    x = 0
    print("\n\n")
    while x < 20:
        print("*", end="")
        x += 1
    print("\n\n")

line_break()

class Person:
    pass

class Student(Person):
    def study(self):
        return 'study..study...study'

p = Person()
try:
    p.study()
except AttributeError as ex:
    print(ex)

s = Student()
print(f"isinstance(s, Person): {isinstance(s, Person)}")
print(f"s.study(): {s.study()}")

line_break()

class Person:
    def routine(self):
        return self.eat() + self.study() + self.sleep()

    def eat(self):
        return 'Person eats...'

    def sleep(self):
        return 'Person sleeps...'

p = Person()
try:
   p.routine()
except AttributeError as ex:
    print(ex)

class Student(Person):
    def study(self):
        return 'Student studies...'

s = Student()
print(f"s.routine(): {s.routine()}")

line_break()

class Person:
    def routine(self):
        result = self.eat()
        if hasattr(self, 'study'):
            result += self.study()
        result += self.sleep()
        return result

    def eat(self):
        return 'Person eats...'

    def sleep(self):
        return 'Person sleeps...'

p = Person()
print(f"p.routine(): {p.routine()}")

class Student(Person):
    def study(self):
        return 'Student studies...'

s = Student()
print(f"s.routine(): {s.routine()}")

line_break()

class Person:
    def __init__(self, name):
        self.name = name

    def routine(self):
        return NotImplemented

p = Person('Alex')
print(f"p.routine(): {p.routine()}")

class Student(Person):
    def routine(self):
        return 'Eat...Study...Sleep'

class Teacher(Person):
    def routine(self):
        return 'Eat...Teach...Sleep'

s = Student('Alex')
t = Teacher('Fred')
print(f"s.routine(): {s.routine()}")
print(f"t.routine(): {t.routine()}")

line_break()

class Account:
    apr = 3.0

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        self.account_type = 'Generic Account'

    def calc_interest(self):
        return f'Calc interest on {self.account_type} with APR = {self.apr}'

a = Account(123, 100)
print(f"a.apr, a.account_type, a.calc_interest(): {a.apr}, {a.account_type}, {a.calc_interest()}")

class Savings(Account):
    apr = 5.0

    def __init__(self, account_number, balance):
        self.account_number = account_number  # We'll revisit this later - this is clumsy
        self.balance = balance
        self.account_type = 'Savings Account'

s = Savings(234, 200)
print(f"s.apr, s.account_type, s.calc_interest(): {s.apr}, {s.account_type}, {s.calc_interest()}")
print(f"Account.apr, Savings.apr: {Account.apr}, {Savings.apr}")

line_break()

class Account:
    apr = 3.0

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        self.account_type = 'Generic Account'

    def calc_interest(self):
        return f'Calc interest on {self.account_type} with APR = {Account.apr}'

class Savings(Account):
    apr = 5.0

    def __init__(self, account_number, balance):
        self.account_number = account_number  # We'll revisit this later - this is clumsy
        self.balance = balance
        self.account_type = 'Savings Account'

s = Savings(123, 100)
print(f"s.calc_interest(): {s.calc_interest()}")
a = Account(123, 100)
s = Savings(234, 200)
print(f"a.__class__: {a.__class__}")
print(f"s.__class__: {s.__class__}")

line_break()

class Account:
    apr = 3.0

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        self.account_type = 'Generic Account'

    def calc_interest(self):
        return f'Calc interest on {self.account_type} with APR = {self.__class__.apr}'

class Savings(Account):
    apr = 5.0

    def __init__(self, account_number, balance):
        self.account_number = account_number  # We'll revisit this later - this is clumsy
        self.balance = balance
        self.account_type = 'Savings Account'

a = Account(123, 100)
s = Savings(234, 200)
print(f"a.calc_interest(), s.calc_interest(): {a.calc_interest()}, {s.calc_interest()}")

s1 = Savings(123, 100)
print(f"s1.__dict__: {s1.__dict__}")
print(f"s1.apr: {s1.apr}")

s2 = Savings(234, 200)
s2.apr = 10
print(f"s2.__dict__: {s2.__dict__}")
print(f"s2.apr: {s2.apr}")

line_break()

class Account:
    apr = 3.0

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        self.account_type = 'Generic Account'

    def calc_interest(self):
        return f'Calc interest on {self.account_type} with APR = {self.apr}'

class Savings(Account):
    apr = 5.0

    def __init__(self, account_number, balance):
        self.account_number = account_number  # We'll revisit this later - this is clumsy
        self.balance = balance
        self.account_type = 'Savings Account'

s1 = Savings(123, 100)
s2 = Savings(234, 200)
s1.apr = 10
print(f"s1.calc_interest(), s2.calc_interest(): {s1.calc_interest()}, {s2.calc_interest()}")

line_break()

class Account:
    apr = 3.0

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        self.account_type = 'Generic Account'

    def calc_interest(self):
        return f'Calc interest on {self.account_type} with APR = {self.__class__.apr}'

class Savings(Account):
    apr = 5.0

    def __init__(self, account_number, balance):
        self.account_number = account_number  # We'll revisit this later - this is clumsy
        self.balance = balance
        self.account_type = 'Savings Account'

s1 = Savings(123, 100)
s2 = Savings(234, 200)
s1.apr = 10
print(f"s1.calc_interest(), s2.calc_interest(): {s1.calc_interest()}, {s2.calc_interest()}")

line_break()

class Account:
    apr = 3.0

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        self.account_type = 'Generic Account'

    def calc_interest(self):
        return f'Calc interest on {self.account_type} with APR = {type(self).apr}'

class Savings(Account):
    apr = 5.0

    def __init__(self, account_number, balance):
        self.account_number = account_number  # We'll revisit this later - this is clumsy
        self.balance = balance
        self.account_type = 'Savings Account'

a = Account(100, 100)
s1 = Savings(101, 100)
s2 = Savings(102, 100)
s2.apr = 10
print(f"a.calc_interest(): {a.calc_interest()}")
print(f"s1.calc_interest(): {s1.calc_interest()}")
print(f"s2.calc_interest(): {s2.calc_interest()}")


