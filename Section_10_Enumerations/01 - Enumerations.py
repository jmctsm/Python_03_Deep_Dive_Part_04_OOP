def line_break():
    x = 0
    print("\n\n")
    while x < 20:
        print("*", end="")
        x += 1
    print("\n\n")

line_break()

import enum

class Color(enum.Enum):
    red = 1
    green = 2
    blue = 3

class Status(enum.Enum):
    PENDING = 'pending'
    RUNNING = 'running'
    COMPLETED = 'completed'

class UnitVector(enum.Enum):
    V1D = (1, )
    V2D = (1, 1)
    V3D = (1, 1, 1)

print(f'Status.PENDING = {Status.PENDING}')
print(f'type(Status.PENDING) = {type(Status.PENDING)}')
print(f'isinstance(Status.PENDING, Status) = {isinstance(Status.PENDING, Status)}')
print(f'Status.PENDING.name , Status.PENDING.value = {Status.PENDING.name , Status.PENDING.value}')
print(f'Status.PENDING is Status.PENDING = {Status.PENDING is Status.PENDING}')
print(f'Status.PENDING == Status.PENDING = {Status.PENDING == Status.PENDING}')

line_break()

class Constants(enum.Enum):
    ONE = 1
    TWO = 2
    THREE = 3

try: 
    Constants.ONE > Constants.TWO
except TypeError as ex:
    print(ex)

line_break()

print(f'Status.PENDING in Status = {Status.PENDING in Status}')
print(f'Status.PENDING.name , Status.PENDING.value = {Status.PENDING.name , Status.PENDING.value}')
#print(f"'PENDING' in Status , 'pending' in Status = {'PENDING' in Status, 'pending' in Status}")

print(f"Status('pending'), UnitVector((1, 1)) = {Status('pending') , UnitVector((1, 1))}")

try:
    print(f"Status('invalid') = {Status('invalid')}")
except ValueError as ex:
    print(ex)

class Person:
    def __init__(self) -> None:
        pass
        
    def __getitem__(self, val):
        return f'__getitem__({val}) called...'

p = Person()
print(f"p['some value'] = {p['some value']}")

print(f"hasattr(Status, '__getitem__') = {hasattr(Status, '__getitem__')}")
print(f'Status.PENDING = {Status.PENDING}')
print(f"getattr(Status, 'PENDING') = {getattr(Status, 'PENDING')}")

class Person:
    __hash__ = None

p = Person()
try:
    print(f'hash(p) = {hash(p)}')
except TypeError as ex:
    print(ex)

class Family(enum.Enum):
    person_1 = Person()
    person_2 = Person()

print(f'Family.person_1 = {Family.person_1}')

family_dict = {Family.person_1: 'person 1', Family.person_2: 'person 2'}

print(f"family_dict = {family_dict}")

line_break()

print(f"hasattr(Status, '__iter__') = {hasattr(Status, '__iter__')}")

for member in Status:
    print(repr(member))

line_break()

class Numbers1(enum.Enum):
    ONE = 1
    TWO = 2
    THREE = 3

class Numbers2(enum.Enum):
    THREE = 3
    TWO = 2
    ONE = 1

print(f'list(Numbers1) = {list(Numbers1)}')
print(f'list(Numbers2) = {list(Numbers2)}')

line_break()

try:
    Status.PENDING.value = 10
except AttributeError as ex:
    print(ex)

#try:
#    Status['NEW'] = 100
#except AttributeError as ex:
#    print(ex)

line_break()

class EnumBase(enum.Enum):
    pass

class EnumExt(EnumBase):
    ONE = 1
    TWO = 2

print(f'EnumExt.ONE = {EnumExt.ONE}')

class EnumBase(enum.Enum):
    ONE = 1

try:
    class EnumExt(EnumBase):
        TWO = 2
except TypeError as ex:
    print(ex)

line_break()

print("EXAMPLE 1")
print(f"Status.PENDING , Status['PENDING'] = {Status.PENDING , Status['PENDING']}")

payload = """
{
    "name": "Alex",
    "status": "PENDING"
}
"""

import json

data = json.loads(payload)

print(f"data['status'] = {data['status']}")
print(f"Status[data['status']] = {Status[data['status']]}")

line_break()

print("EXAMPLE 2")

def is_member(en, name):
    try:
        en[name]
    except KeyError:
        return False
    return True

print(f"is_member(Status, 'PENDING') = {is_member(Status, 'PENDING')}")
print(f"is_member(Status, 'pending') = {is_member(Status, 'pending')}")

print(f"getattr(Status, 'PENDING', None) , getattr(Status, 'OK', None) = {getattr(Status, 'PENDING', None), getattr(Status, 'OK', None)}")


print(f'Status.__members__ = {Status.__members__}')
print(f"'PENDING' in Status.__members__ = {'PENDING' in Status.__members__}")
print(f"'PENDING' in Status.__members__.keys() = {'PENDING' in Status.__members__.keys()}")