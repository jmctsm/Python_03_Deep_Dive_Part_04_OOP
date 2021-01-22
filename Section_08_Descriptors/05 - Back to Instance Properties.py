def line_break():
    x = 0
    print("\n\n")
    while x < 20:
        print("*", end="")
        x += 1
    print("\n\n")


line_break()

import weakref
import ctypes

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

line_break()

class IntegerValue:
    def __init__(self):
        self.values = weakref.WeakKeyDictionary()

    def __set__(self, instance, value):
        self.values[instance] = int(value)

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return self.values.get(instance)

class Point:
    x = IntegerValue()

p = Point()
print(f'hex(id(p)) = {hex(id(p))}')
p.x = 100.1
print(f'p.x = {p.x}')
print(f'Point.x.values.keyrefs() = {Point.x.values.keyrefs()}')

del p
print(f'Point.x.values.keyrefs() = {Point.x.values.keyrefs()}')

line_break()

class IntegerValue:
    def __init__(self):
        self.values = {}

    def __set__(self, instance, value):
        self.values[id(instance)] = int(value)

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return self.values.get(id(instance))

class Point:
    x = IntegerValue()

    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x

p = Point(10.1)
print(f'p.x = {p.x}')
p.x = 20.2
print(f'p.x = {p.x}')
print(f'id(p) , Point.x.values = {id(p)} , {Point.x.values}')

def ref_count(address):
    return ctypes.c_long.from_address(address).value

p_id = id(p)
print(f'ref_count(p_id) = {ref_count(p_id)}')
del p
print(f'ref_count(p_id) = {ref_count(p_id)}')
print(f'Point.x.values = {Point.x.values}')

p = Point(10.1)
weak_p = weakref.ref(p)

print(f'hex(id(p)) , weak_p = {hex(id(p))} , {weak_p}')
print(f'ref_count(id(p)) = {ref_count(id(p))}')

del p
print(f'weak_p = {weak_p}')

def obj_destroyed(obj):
    print(f'{obj} is being destroyed')

p = Point(10.1)
w = weakref.ref(p, obj_destroyed)

del p

line_break()

class IntegerValue:
    def __init__(self):
        self.values = {}

    def __set__(self, instance, value):
        self.values[id(instance)] = (weakref.ref(instance, self._remove_object), int(value))

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            value_tuple = self.values.get(id(instance))
            return value_tuple[1] # return the associated value, not the weak ref

    def _remove_object(self, weak_ref):
        print(f'removing dead entry for {weak_ref}')
        # how do we find that weak reference


class Point:
    x = IntegerValue()

p1 = Point()
p2 = Point()

p1.x, p2.x = 10.1, 100.1

print(f'p1.x , p2.x = {p1.x} , {p2.x}')
print(f'ref_count(id(p1)) , ref_count(id(p2)) = {ref_count(id(p1))} , {ref_count(id(p2))}')

del p1

del p2

line_break()

class IntegerValue:
    def __init__(self):
        self.values = {}

    def __set__(self, instance, value):
        self.values[id(instance)] = (weakref.ref(instance, self._remove_object), int(value))

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            value_tuple = self.values.get(id(instance))
            return value_tuple[1] # return the associated value, not the weak ref

    def _remove_object(self, weak_ref):
        reverse_lookup = [key for key, value in self.values.items()
                          if value[0] is weak_ref]
        if reverse_lookup:
            # key found
            key = reverse_lookup[0]
            del self.values[key]


class Point:
    x = IntegerValue()

p = Point()
p.x = 10.1
print(f'p.x = {p.x}')
print(f'Point.x.values = {Point.x.values}')
print(f'ref_count(id(p)) = {ref_count(id(p))}')
del p

print(f'Point.x.values = {Point.x.values}')

line_break()

class Person:
    pass

print(f'Person.__dict__ = {Person.__dict__}')
print(f"hasattr(Person.__weakref__, '__get__') , hasattr(Person.__weakref__, '__set__') = "
      f"{hasattr(Person.__weakref__, '__get__')} , {hasattr(Person.__weakref__, '__set__')}")

p = Person()
print(f"hasattr(p, '__weakref__') = {hasattr(p, '__weakref__')}")
print(f'p.__weakref__ = {p.__weakref__}')

w = weakref.ref(p)
print(f'p.__weakref__ = {p.__weakref__}')

line_break()

class Person:
    __slots__ = 'name',

print(f'Person.__dict__ = {Person.__dict__}')

p = Person()
print(f"hasattr(p, '__weakref__') = {hasattr(p, '__weakref__')}")

try:
    weakref.ref(p)
except TypeError as ex:
    print(ex)

line_break()

class Person:
    __slots__ = 'name', '__weakref__',

print(f'Person.__dict__ = {Person.__dict__}')

p = Person()
print(f"hasattr(p, '__weakref__') = {hasattr(p, '__weakref__')}")

w = weakref.ref(p)
print(f'p.__weakref__ = {p.__weakref__}')

line_break()

class ValidString:
    def __init__(self, min_length=0, max_length=255):
        self.data = {}
        self._min_length = min_length
        self._max_length = max_length

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError('Value must be a string.')
        if len(value) < self._min_length:
            raise ValueError(f'Value should be at least {self._min_length} characters.')
        if len(value) > self._max_length:
            raise ValueError(f'Value cannot exceed {self._max_length} characters.')
        self.data[id(instance)] = (weakref.ref(instance, self._finalize_instance), value)

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            value_tuple = self.data.get(id(instance))
            return value_tuple[1]

    def _finalize_instance(self, weak_ref):
        reverse_lookup = [key for key, value in self.data.items()
                          if value[0] is weak_ref]
        if reverse_lookup:
            # key found
            key = reverse_lookup[0]
            del self.data[key]

class Person:
    __slots__ = '__weakref__',

    first_name = ValidString(1, 100)
    last_name = ValidString(1,100)

    def __eq__(self, other):
        return (isinstance(other, Person) and
                self.first_name == other.first_name and
                self.last_name == other.last_name)

class BankAccount:
    __slots__ = '__weakref__',

    account_number = ValidString(5,255)

    def __eq__(self, other):
        return (isinstance(other, BankAccount) and self.account_number == other.account_number)

p1 = Person()

try:
    p1.first_name = ''
except ValueError as ex:
    print(ex)

p2 = Person()
p1.first_name, p1.last_name = 'Guido', 'van Rossum'
p2.first_name, p2.last_name = 'Raymond', 'Hettinger'

b1, b2 = BankAccount(), BankAccount()

b1.account_number, b2.account_number = 'Savings', 'Checking'

print(f'p1.first_name , p1.last_name = {p1.first_name} , {p1.last_name}')
print(f'p2.first_name , p2.last_name = {p2.first_name} , {p2.last_name}')
print(f'b1.account_number , b2.account_number = {b1.account_number} , {b2.account_number}')

print(f'Person.first_name.data = {Person.first_name.data}')
print(f'Person.last_name.data = {Person.last_name.data}')
print(f'BankAccount.account_number.data = {BankAccount.account_number.data}')

del p1
del p2
del b1
del b2

print(f'Person.first_name.data = {Person.first_name.data}')
print(f'Person.last_name.data = {Person.last_name.data}')
print(f'BankAccount.account_number.data = {BankAccount.account_number.data}')
