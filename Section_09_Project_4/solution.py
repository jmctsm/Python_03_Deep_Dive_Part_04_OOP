import numbers

def line_break():
    x = 0
    print("\n\n")
    while x < 20:
        print("*", end="")
        x += 1
    print("\n\n")

line_break()

class IntegerField:
    def __init__(self, min_, max_) -> None:
        self._min = min_
        self._max = max_

    def __set_name__(self, owner_class, prop_name):
        self.prop_name = prop_name

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError(f'{self.prop_name} must be an integer')
        if value < self._min:
            raise ValueError(f'{self.prop_name} must be >= {self._min}')
        if value > self._max:
            raise ValueError(f'{self.prop_name} must be <= {self._max}')
        instance.__dict__[self.prop_name] = value

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return instance.__dict__.get(self.prop_name, None)

# class Person:
#     age = IntegerField(0, 100)

# p = Person()

# p.age = 5

# print(f'p.age = {p.age}')

# try:
#     p.age = 200
# except ValueError as ex:
#     print(ex)

# Person = type('Person', (), {'a': 10})
# print(f'type(Person) = {type(Person)}')
# print(f'Person.__dict__ = {Person.__dict__}')

# class Person:
#     age = 10

# print(f'type(Person) = {type(Person)}')
# print(f'Person.__dict__ = {Person.__dict__}')

line_break()

class IntegerField:
    def __init__(self, min_, max_):
        self._min = min_
        self._max = max_

    def __set_name__(self, owner_class, prop_name):
        self.prop_name = prop_name

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError(f'{self.prop_name} must be an integer')
        if self._min is not None and value < self._min:
            raise ValueError(f'{self.prop_name} must be >= {self._min}')
        if self._max is not None and value > self._max:
            raise ValueError(f'{self.prop_name} must be <= {self._max}')
        instance.__dict__[self.prop_name] = value

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return instance.__dict__.get(self.prop_name, None)

line_break()

class CharField:
    def __init__(self, min_=None, max_=None) -> None:
        min_ = min_ or 0 # in case min_ is None
        min_ = max(min_, 0) # replaces negative value with zero
        self._min = min_
        self._max = max_

    def __set_name__(self, owner_class, prop_name):
        self.prop_name = prop_name

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f'{self.prop_name} must be a string')
        if self._min is not None and len(value) < self._min:
            raise ValueError(f'{self.prop_name} must be >= {self._min} chars.')
        if self._max is not None and len(value) > self._max:
            raise ValueError(f'{self.prop_name} must be <= {self._max} chars')
        instance.__dict__[self.prop_name] = value

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return instance.__dict__.get(self.prop_name, None)

class Person:
    name = CharField(1, 10)

p = Person()

try:
    p.name = ""
except ValueError as ex:
    print(ex)

try:
    p.name = "Python ROCKS!!"
except ValueError as ex:
    print(ex)

p.name = "John"

line_break()

class Person:
    name = CharField(-10, 10)

p = Person()
p.name = ""
print(f'p.name = {p.name}')

line_break()

class Person:
    name = CharField(1)

p = Person()
p.name = "I'm a lumberjack and I'm OK, I sleep all night and I work all day."
print(f'p.name = {p.name}')

line_break()

class BaseValidator:
    def __init__(self, min_=None, max_=None):
        self._min = min_
        self._max = max_

    def __set_name__(self, owner_class, prop_name):
        self.prop_name = prop_name

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return instance.__dict__.get(self.prop_name, None)

    def validate(self, value):
        # this will need to be implemented specifically by each subclass
        # here we just default to not raising any exceptions
        pass

    def __set__(self, instance, value):
        self.validate(value)
        instance.__dict__[self.prop_name] = value

class Person:
    name = BaseValidator()

p = Person()
p.name = 'Alex'
print(f'p.name = {p.name}')

class IntegerField(BaseValidator):
    def validate(self, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError(f'{self.prop_name} must be an integer')
        if self._min is not None and value < self._min:
            raise ValueError(f'{self.prop_name} must be >= {self._min}')
        if self._max is not None and value > self._max:
            raise ValueError(f'{self.prop_name} must be <= {self._max}')

class CharField(BaseValidator):
    def __init__(self, min_, max_):
        min_ = max(min_ or 0, 0)
        super().__init__(min_, max_)

    def validate(self, value):
        if not isinstance(value, str):
            raise ValueError(f'{self.prop_name} must be a string')
        if self._min is not None and len(value) < self._min:
            raise ValueError(f'{self.prop_name} must be >= {self._min} chars.')
        if self._max is not None and len(value) > self._max:
            raise ValueError(f'{self.prop_name} must be <= {self._max} chars')
