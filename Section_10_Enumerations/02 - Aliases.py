def line_break():
    x = 0
    print("\n\n")
    while x < 20:
        print("*", end="")
        x += 1
    print("\n\n")

line_break()

import enum

class NumSides(enum.Enum):
    Triangle = 3
    Rectangle = 4
    Square = 4
    Rhombus = 4

print(f'NumSides.Rectangle is NumSides.Square = {NumSides.Rectangle is NumSides.Square}')

print(f'NumSides.Square is NumSides.Rhombus = {NumSides.Square is NumSides.Rhombus}')

print(f'NumSides.Square in NumSides = {NumSides.Square in NumSides}')

print(f'NumSides(4) = {NumSides(4)}')

print(f'list(NumSides) = {list(NumSides)}')

print(f'NumSides.__members__ = {NumSides.__members__}')

line_break()

print("EXAMPLE")

class Status(enum.Enum):
    ready = 'ready'

    running = 'running'
    busy = 'running'
    processing = 'running'

    ok = 'ok'
    finished_no_error = 'ok'
    ran_ok = 'ok'

    errors = 'errors'
    finished_with_errors= 'errors'
    errored= 'errors'

print(f'list(Status) = {list(Status)}')

print(f"Status['busy'] = {Status['busy']}")

print(f"Status['processing'] = {Status['processing']}")

line_break()

class Status(enum.Enum):
    ready = 1

    running = 2
    busy = 2
    processing = 2

    ok = 3
    finished_no_error = 3
    ran_ok = 3

    errors = 4
    finished_with_errors = 4
    errored = 4

print(f"Status.ran_ok = {Status.ran_ok}")
# print(f"status in Status.__members__ = {status in Status.__members__}")

line_break()

print("ENSURING NO ALIASES")

@enum.unique
class Status(enum.Enum):
    ready = 1
    done_ok = 2
    errors = 3

try:
    @enum.unique
    class Status(enum.Enum):
        ready = 1
        waiting = 1
        done_ok = 2
        errors = 3
except ValueError as ex:
    print(ex)
    