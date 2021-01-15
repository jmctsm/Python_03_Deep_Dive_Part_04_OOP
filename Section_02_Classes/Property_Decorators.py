def line_break():
    x = 0
    while x < 20:
        print("*", end="")
        x += 1
    print("\n")

p = property(fget=lambda self: print('getting property'))
print(p)

line_break()

def my_decorator(fn):
    print('decorating function')
    def inner(*args, **kwargs):
        print('Running decorated function')
        return fn(*args, **kwargs)
    return inner

def undecorated_function(a, b):
    print('running original function')
    return a + b

decorated_func = my_decorator(undecorated_function)
print(decorated_func(10, 20))
line_break()

def my_func(a, b):
    print('Running original function')
    return a + b

my_func = my_decorator(my_func)
print(my_func)
print(my_func(10, 20))

line_break()

@my_decorator
def my_func(a, b):
    print("Running original function")
    return a + b

print(my_func(20, 20))

line_break()

class Person:
    def __init__(self, name):
        self._name = name

    def name(self):
        return self._name

    name = property(name)

p = Person("ALex")
print(p.name)
print(p.__dict__)
print(Person.__dict__)

line_break()

class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

p = Person("Guido")
print(p.name)

line_break()

p = property(lambda self: 'getter')

print(dir(p))
print(p)
p2 = p.setter(lambda self: 'setter')
print(id(p), id(p2))

line_break()

class Person:
    def __init__(self, name):
        self._name = name

    def name(self):
        return self._name

    name = property(name)

    # Creating another symbol that holds on to the name property
    name_prop = name

    # because here I'm redefining name, so we lose our original reference to the property object
    def name(self, value):
        self._name = value

    name = name_prop.setter(name)

    # finally delete name_prop which we no longer need
    del name_prop

print(Person.__dict__)
p = Person('ALex')
print(p.name)

p.name = 'Raymond'
print(p.name)

line_break()

class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    # what's the property name now? --> name
    # so name has a setter callable
    @name.setter
    def name(self, value):
        self._name = value

print(Person.__dict__)
p = Person("Alex")
print(p.name)

p.name = "Guido"
print(p.name)

line_break()

class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    # property is now called name

    @name.setter
    def full_name(self, value):
        self._name = value

print(Person.__dict__)
p = Person("alex")
print(p.name)
print(p.full_name)
p.full_name = "Raymond"
print(p.full_name)
try:
    p.name = "Guido"
except AttributeError as ex:
    print(ex)

line_break()

class Person:
    def __init__(self, name):
        self._name = name

    name = property() # an "empty" property - no getter or setter

    @name.setter
    def name(self, value):
        self._name = value

    @name.getter
    def name(self):
        return self._name

p = Person("Jimmy")
print(p.name)
p.name = "Kelly"
print(p.name)

line_break()

class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        """The Person's name"""
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

print(help(Person))
print(help(Person.name))

line_break()

class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        """The Person's name"""
        self._name = value


print(help(Person.name))
print(help(Person))

line_break()

class Person:
    def __init__(self, name):
        self._name = name

    name = property(doc="Write-only name property")

    @name.setter
    def name(self, value):
        self._name = value


print(help(Person.name))
print(help(Person))


