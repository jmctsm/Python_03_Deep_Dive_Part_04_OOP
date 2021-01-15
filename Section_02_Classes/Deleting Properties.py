def line_break():
    x = 0
    while x < 20:
        print("*", end="")
        x += 1
    print("\n")

class Person:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        print('Getting name property value...')
        return self._name

    def set_name(self, value):
        print(f'setting name property to {value}...')
        self._name = value

    def del_name(self):
        # delete the underlying data
        print('Deleting name property value...')
        del self._name

    name = property(fget=get_name, fset=set_name, fdel=del_name, doc='Person name.')


p = Person('Kelly')
print(p.name)
print(p.__dict__)
del p.name
print(p.__dict__)
try:
    print(p.name)
except AttributeError as ex:
    print(ex)

line_break()
line_break()

p = Person('Emily')
print(p.__dict__)
delattr(p, 'name')
print(p.__dict__)

line_break()
line_break()

class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        print('Getting name property value...')
        return self._name

    @name.setter
    def name(self, value):
        """Person name"""
        print(f'setting name property to {value}...')
        self._name = value

    @name.deleter
    def name(self):
        # delete the underlying data
        print('Deleting name property value...')
        del self._name


p = Person("Wench")
print(p.__dict__)
print(p.name)
del p.name
print(p.__dict__)