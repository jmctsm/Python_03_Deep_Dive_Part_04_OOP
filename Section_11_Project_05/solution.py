class GenericException(Exception):
    pass


class TimeOut(Exception):
    pass


from enum import Enum


class AppException(Enum):
    Generic = (100, GenericException, "Application Exception")
    Timeout = (101, TimeOut, "Timeout connecting to resource")
    NotAnInteger = (200, ValueError, "Value must be an integer")
    NotAList = (201, ValueError, "Value must be a list")

    def __new__(cls, ex_code, ex_class, ex_message):
        # create a new instance of cls
        member = object.__new__(cls)

        # setup instance atttributes
        member._value_ = ex_code
        member.exception = ex_class
        member.message = ex_message
        return member


print(
    f"AppException.Timeout.value , AppException.Timeout.message , AppException.Timeout.exception = {AppException.Timeout.value , AppException.Timeout.message , AppException.Timeout.exception}"
)

try:
    raise AppException.Timeout.exception(
        f"{AppException.Timeout.value} - {AppException.Timeout.message}"
    )
except TimeOut as ex:
    print(ex)

print("\n\n\n")


class AppException(Enum):
    Generic = (100, GenericException, "Application Exception")
    TimeOut = (101, TimeOut, "Timeout connecting to resource")
    NotAnInteger = (200, ValueError, "Value must be an integer")
    NotAList = (201, ValueError, "Value must be a list")

    def __new__(cls, ex_code, ex_class, ex_message):
        # create a new instance of cls
        member = object.__new__(cls)

        # setup instance atttributes
        member._value_ = ex_code
        member.exception = ex_class
        member.message = ex_message
        return member

    @property
    def code(self):
        return self.value

    def throw(self):
        raise self.exception(f"{self.code} - {self.message}")


try:
    AppException.NotAnInteger.throw()
except ValueError as ex:
    print(ex)

print(
    f"AppException.NotAList.code , AppException.NotAList.message = {AppException.NotAList.code , AppException.NotAList.message}"
)

print(
    f"AppException(201) , AppException['NotAList'] = {AppException(201) , AppException['NotAList']}"
)

print("\n\n\n")


class AppException(Enum):
    Generic = (100, GenericException, "Application Exception")
    TimeOut = (101, TimeOut, "Timeout connecting to resource")
    NotAnInteger = (200, ValueError, "Value must be an integer")
    NotAList = (201, ValueError, "Value must be a list")

    def __new__(cls, ex_code, ex_class, ex_message):
        # create a new instance of cls
        member = object.__new__(cls)

        # setup instance atttributes
        member._value_ = ex_code
        member.exception = ex_class
        member.message = ex_message
        return member

    @property
    def code(self):
        return self.value

    def throw(self, message=None):
        message = message or self.message
        raise self.exception(f"{self.code} - {self.message}")


try:
    AppException.TimeOut.throw("Timeout connecting to database")
except Exception as ex:
    print(ex)

print(f"list(AppException) = {list(AppException)}")

print(
    f"[(ex.name, ex.code, ex.message) for ex in AppException] = {[(ex.name, ex.code, ex.message) for ex in AppException]}"
)
