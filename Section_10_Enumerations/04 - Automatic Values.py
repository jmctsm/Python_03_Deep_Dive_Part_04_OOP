def line_break():
    x = 0
    print("\n\n")
    while x < 20:
        print("*", end="")
        x += 1
    print("\n\n")


line_break()

import enum


class State(enum.Enum):
    WAITING = enum.auto()
    STARTED = enum.auto()
    FINISHED = enum.auto()


for member in State:
    print(f"member.name , member.value = {member.name , member.value}")

line_break()


class State(enum.Enum):
    WAITING = 5
    STARTED = enum.auto()
    FINISHED = enum.auto()


for member in State:
    print(f"member.name , member.value = {member.name , member.value}")


line_break()


class State(enum.Enum):
    WAITING = enum.auto()
    STARTED = 1
    FINISHED = enum.auto()


for member in State:
    print(f"member.name , member.value = {member.name , member.value}")

print(f"State.__members__ = {State.__members__}")

try:

    @enum.unique
    class State(enum.Enum):
        WAITING = enum.auto()
        STARTED = 1
        FINISHED = enum.auto()


except ValueError as ex:
    print(ex)

line_break()


class State(enum.Enum):
    def _generate_next_value_(name, start, count, last_values):
        print(
            f"name , start , count , last_values = {name , start , count , last_values}"
        )
        return 100

    a = enum.auto()
    b = enum.auto()
    c = enum.auto()


print(f"State.__members__ = {State.__members__}")

line_break()

import random

random.seed(0)


class State(enum.Enum):
    def _generate_next_value_(name, start, count, last_values):
        while True:
            new_value = random.randint(1, 100)
            if new_value not in last_values:
                return new_value

    a = enum.auto()
    b = enum.auto()
    c = enum.auto()


for member in State:
    print(f"member.name , member.value = {member.name , member.value}")

print(f"State.__members__ = {State.__members__}")

line_break()


class State(enum.Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name.title()

    WAITING = enum.auto()
    STARTED = enum.auto()
    FINISHED = enum.auto()


for member in State:
    print(f"member.name , member.value = {member.name , member.value}")

print(f"State.__members__ = {State.__members__}")

line_break()


class NameAsString(enum.Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name.lower()


class Enum1(NameAsString):
    A = enum.auto()
    B = enum.auto()


class Enum2(NameAsString):
    WAITING = enum.auto()
    RUNNING = enum.auto()
    FINISHED = enum.auto()


for member in Enum1:
    print(f"member.name , member.value = {member.name , member.value}")

print(f"Enum1.__members__ = {Enum1.__members__}")


for member in Enum2:
    print(f"member.name , member.value = {member.name , member.value}")

print(f"Enum2.__members__ = {Enum2.__members__}")

line_break()

print("Note")


class State(enum.Enum):
    WAIT = object()
    RUNNING = object()
    FINISHED = object()


print(
    f"State.WAIT , State.RUNNING , State.FINISHED = {State.WAIT, State.RUNNING, State.FINISHED}"
)


class ValueLessEnum(enum.Enum):
    def _generate_next_value_(name, start, count, last_values):
        return object()


class State(ValueLessEnum):
    WAIT = enum.auto()
    RUNNING = enum.auto()
    FINISHED = enum.auto()


class Errors(ValueLessEnum):
    NumberError = enum.auto()
    IndexError = enum.auto()
    TimeoutError = enum.auto()


print(f"State.WAIT , Errors.TimeoutError = {State.WAIT , Errors.TimeoutError}")


class ValueLessEnum(enum.Enum):
    def _generate_next_value_(name, start, count, last_values):
        while True:
            new_value = random.randint(1, 100)
            if new_value not in last_values:
                return new_value


class State(ValueLessEnum):
    WAIT = enum.auto()
    RUNNING = enum.auto()
    FINISHED = enum.auto()


class Errors(ValueLessEnum):
    NumberError = enum.auto()
    IndexError = enum.auto()
    TimeoutError = enum.auto()


print(f"State.WAIT , Errors.TimeoutError = {State.WAIT , Errors.TimeoutError}")

line_break()

print("Auto and Aliases")


class Aliased(enum.Enum):
    def _generate_next_value_(name, start, count, last_values):
        print(f"count = {count}")
        if count % 2 == 1:
            # add, mae this member an alias of the previous one
            return last_values[-1]
        else:
            # make a new value
            return last_values[-1] + 1

    GREEN = 1
    GREEN_ALIAS = 1
    RED = 10
    CRIMSON = enum.auto()
    BLUE = enum.auto()
    AQUA = enum.auto()


print(f"list(Aliased) = {list(Aliased)}")
print(f"Aliased.__members__ = {Aliased.__members__}")
