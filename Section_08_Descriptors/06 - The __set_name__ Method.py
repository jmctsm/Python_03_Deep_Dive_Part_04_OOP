def line_break():
    x = 0
    print("\n\n")
    while x < 20:
        print("*", end="")
        x += 1
    print("\n\n")


line_break()

class ValidString:
    def __set_name__(self, owner_class, property_name):
        print(f'__set_name__ called: owner={owner_class} , prop={property_name}')

class Person:
    name = ValidString()

line_break()

class ValidString:
    def __set_name__(self, owner_class, property_name):
        print(f'__set_name__ called: owner={owner_class} , prop={property_name}')
        self.property_name = property_name

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            print(f'__get__ called for property {self.property_name} of instance {instance}')


class Person:
    first_name = ValidString()
    last_name = ValidString()

p = Person()
print(f'p.first_name = {p.first_name}')

line_break()

class ValidString:
    def __init__(self, min_length):
        self.min_length = min_length

    def __set_name__(self, owner_class, property_name):
        self.property_name = property_name

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f'{self.property_name} must be a string')
        if len(value) < self.min_length:
            raise ValueError(f'{self.property_name} must be at least {self.min_length} characters')
        key = '_' + self.property_name
        setattr(instance, key, value)

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            key = '_' + self.property_name
            return getattr(instance, key, None)

class Person:
    first_name = ValidString(1)
    last_name = ValidString(2)

p = Person()
try:
    p.first_name = 'Alex'
    p.last_name = 'M'
except ValueError as ex:
    print(ex)

p = Person()
p.first_name = 'Alex'

print(f'p.first_name , p.__dict__ = {p.first_name} , {p.__dict__}')

p = Person()
p._first_name = 'some data I need to store'
print(f'p.first_name , p.__dict__ = {p.first_name} , {p.__dict__}')
p.first_name = 'Alex'
print(f'p.first_name , p.__dict__ = {p.first_name} , {p.__dict__}')


line_break()


class BankAccount:
    apr = 10

b = BankAccount()

print(f'b.apr , b.__dict__ = {b.apr} , {b.__dict__}')
b.apr = 20
print(f'b.apr , b.__dict__ = {b.apr} , {b.__dict__}')

line_break()

class ValidString:
    def __init__(self, min_length):
        self.min_length = min_length

    def __set_name__(self, owner_class, property_name):
        self.property_name = property_name

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f'{self.property_name} must be a string')
        if len(value) < self.min_length:
            raise ValueError(f'{self.property_name} must be at least {self.min_length} characters')
        instance.__dict__[self.property_name] = value

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            print(f'Calling __get__ for {self.property_name}')
            return instance.__dict__.get(self.property_name, None)

class Person:
    first_name = ValidString(1)
    last_name = ValidString(2)

p = Person()

print(f'p.__dict__ = {p.__dict__}')

p.first_name = 'Alex'
print(f'p.__dict__ = {p.__dict__}')
print(f'p.first_name = {p.first_name}')