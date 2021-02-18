def line_break():
    x = 0
    print("\n\n")
    while x < 20:
        print("*", end="")
        x += 1
    print("\n\n")


line_break()

from enum import Enum
from typing import OrderedDict, Type


class Color(Enum):
    red = 1
    green = 2
    blue = 3

    def purecolor(self, value):
        return {self: value}


print(
    f"Color.red.purecolor(100) , Color.blue.purecolor(200) = {Color.red.purecolor(100) , Color.blue.purecolor(200)}"
)


class Color(Enum):
    red = 1
    green = 2
    blue = 3

    def __repr__(self):
        return f"{self.name} ({self.value})"


print(f"repr(Color.red) = {repr(Color.red)}")

line_break()


class Number(Enum):
    ONE = 1
    TWO = 2
    THREE = 3


try:
    print(f"Number.ONE > Number.TWO = {Number.ONE > Number.TWO}")
except TypeError as ex:
    print(ex)


class Number(Enum):
    ONE = 1
    TWO = 2
    THREE = 3

    def __lt__(self, other):
        return isinstance(other, Number) and self.value < other.value


try:
    print(f"Number.ONE < Number.TWO = {Number.ONE < Number.TWO}")
    print(f"Number.TWO > Number.ONE = {Number.TWO > Number.ONE}")
except TypeError as ex:
    print(ex)

line_break()


class Number(Enum):
    ONE = 1
    TWO = 2
    THREE = 3

    def __lt__(self, other):
        return isinstance(other, Number) and self.value < other.value

    def __eq__(self, other):
        if isinstance(other, Number):
            return self is other
        elif isinstance(other, int):
            return self.value == other
        else:
            return False


print(f"Number.ONE == Number.ONE = {Number.ONE == Number.ONE}")
print(f"Number.ONE == 1.0 = {Number.ONE == 1.0}")
print(f"Number.ONE == 1 = {Number.ONE == 1}")

try:
    print(f"hash(Number.ONE) = {hash(Number.ONE)}")
except TypeError as ex:
    print(ex)

try:
    print(f"Number.ONE <= Number.TWO = {Number.ONE <= Number.TWO}")
except TypeError as ex:
    print(ex)

from functools import total_ordering


@total_ordering
class Number(Enum):
    ONE = 1
    TWO = 2
    THREE = 3

    def __lt__(self, other):
        return isinstance(other, Number) and self.value < other.value


try:
    print(f"Number.ONE <= Number.TWO = {Number.ONE <= Number.TWO}")
    print(f"Number.ONE != Number.TWO = {Number.ONE != Number.TWO}")
except TypeError as ex:
    print(ex)

line_break()


class Phase(Enum):
    READY = "ready"
    RUNNING = "running"
    FINISHED = "finished"

    def __str__(self):
        return self.value

    def __eq__(self, other):
        if isinstance(other, Phase):
            return self is other
        elif isinstance(other, str):
            return self.value == other
        return False

    def __lt__(self, other):
        ordered_items = list(Phase)
        self_order_index = ordered_items.index(self)

        if isinstance(other, Phase):
            other_order_index = ordered_items.index(other)
            return self_order_index < other_order_index

        if isinstance(other, str):
            try:
                other_member = Phase(other)
                other_order_index = ordered_items.index(other_member)
                return self_order_index < other_order_index
            except ValueError:
                # other is not a value in our enum
                return False


print(f"Phase.READY == 'ready' = {Phase.READY == 'ready'}")
print(f"Phase.READY < Phase.RUNNING = {Phase.READY < Phase.RUNNING}")
print(f"Phase.READY < 'running' = {Phase.READY < 'running'}")

line_break()


class State(Enum):
    READY = 1
    BUSY = 0


print(f"bool(State.READY) , bool(State.BUSY) = {bool(State.READY) , bool(State.BUSY)}")


class State(Enum):
    READY = 1
    BUSY = 0

    def __bool__(self):
        return bool(self.value)


print(f"bool(State.READY) , bool(State.BUSY) = {bool(State.READY) , bool(State.BUSY)}")

request_state = State.READY
if request_state:
    print("Launching next query")
else:
    print("Not Ready for another query yet")


class Dummy(Enum):
    A = 0
    B = 1
    C = ""
    D = "python"

    def __bool__(self):
        return bool(self.value)


print(
    f"bool(Dummy.A), bool(Dummy.B), bool(Dummy.C), bool(Dummy.D) = {bool(Dummy.A), bool(Dummy.B), bool(Dummy.C), bool(Dummy.D)}"
)

line_break()

print("Extending Custom Enumerations")


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


try:

    class ColorAlpha(Color):
        ALPHA = 4


except TypeError as ex:
    print(ex)


class ColorBase(Enum):
    def hello(self):
        return f"{str(self)} says HELLO!"


class Color(ColorBase):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"


Color.RED.hello()


@total_ordering
class OrderedEnum(Enum):
    """Creates an ordering based on the member values.
    So member values have to support rich comparisons.
    """

    def __lt__(self, other):
        if isinstance(other, OrderedEnum):
            return self.value < other.value
        return NotImplemented


class Number(OrderedEnum):
    ONE = 1
    TWO = 2
    THREE = 3


class Dimension(OrderedEnum):
    D1 = (1,)
    D2 = 1, 1
    D3 = 1, 1, 1


print(f"Number.ONE < Number.THREE = {Number.ONE < Number.THREE}")
print(f"Dimension.D1 < Dimension.D3 = {Dimension.D1 < Dimension.D3}")
print(f"Number.ONE >= Number.ONE = {Number.ONE >= Number.ONE}")
print(f"Dimension.D1 >= Dimension.D2 = {Dimension.D1 >= Dimension.D2}")

line_break()

print("Example")

from http import HTTPStatus

print(f"type(HTTPStatus) = {type(HTTPStatus)}")
print(f"list(HTTPStatus)[0:10] = {list(HTTPStatus)[0:10]}")
print(f"HTTPStatus(200) = {HTTPStatus(200)}")
print(
    f"HTTPStatus.OK, HTTPStatus.OK.name, HTTPStatus.OK.value = {HTTPStatus.OK, HTTPStatus.OK.name, HTTPStatus.OK.value}"
)

print(f"HTTPStatus(200) = {HTTPStatus(200)}")
print(f"HTTPStatus['OK'] = {HTTPStatus['OK']}")
print(
    f"HTTPStatus.NOT_FOUND.value, HTTPStatus.NOT_FOUND.name, HTTPStatus.NOT_FOUND.phrase = {HTTPStatus.NOT_FOUND.value, HTTPStatus.NOT_FOUND.name, HTTPStatus.NOT_FOUND.phrase}"
)


class AppStatus(Enum):
    OK = (0, "No Problem")
    FAILED = (1, "CRAP!")


print(f"AppStatus.OK = {AppStatus.OK}")
print(f"AppStatus.OK.value = {AppStatus.OK.value}")


class AppStatus(Enum):
    OK = (0, "No Problem")
    FAILED = (1, "CRAP!")

    @property
    def code(self):
        return self.value[0]

    @property
    def phrase(self):
        return self.value[1]


print(
    f"AppStatus.OK.code , AppStatus.OK.phrase = {AppStatus.OK.code , AppStatus.OK.phrase}"
)

try:
    print(f"AppStatus(0) = {AppStatus(0)}")
except ValueError as ex:
    print(ex)

# print(f"AppStatus((0, 'No problem!')) = {AppStatus((0, 'No problem!'))}")

line_break()

print("Let's dig in")


class AppStatus(Enum):
    OK = (0, "No Problem!")
    FAILED = (1, "Crap!")

    def __new__(cls, member_value, member_phrase):
        # Create a new instance of cls
        member = object.__new__(cls)

        # setup instance variables
        member._value_ = member_value
        member.phrase = member_phrase
        return member


print(
    f"AppStatus.OK.value, AppStatus.OK.name, AppStatus.OK.phrase = {AppStatus.OK.value, AppStatus.OK.name, AppStatus.OK.phrase}"
)

print(f"AppStatus(0) = {AppStatus(0)}")


class TwoValueEnum(Enum):
    def __new__(cls, member_value, member_phrase):
        member = object.__new__(cls)
        member._value_ = member_value
        member.phrase = member_phrase
        return member


class AppStatus(TwoValueEnum):
    OK = (0, "No Problem!")
    FAILED = (1, "Crap!")


print(
    f"AppStatus.FAILED, AppStatus.FAILED.name, AppStatus.FAILED.value, AppStatus.FAILED.phrase = {AppStatus.FAILED, AppStatus.FAILED.name, AppStatus.FAILED.value, AppStatus.FAILED.phrase}"
)
