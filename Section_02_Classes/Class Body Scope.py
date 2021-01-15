def line_break():
    x = 0
    print("\n\n")
    while x < 20:
        print("*", end="")
        x += 1
    print("\n\n")


class Language:
    MAJOR = 3
    MINOR = 7
    REVISION = 4
    FULL = '{}.{}.{}'.format(MAJOR, MINOR, REVISION)


print(Language.FULL)

line_break()

class Language:
    MAJOR = 3
    MINOR = 7
    REVISION = 4
    FULL = '{}.{}.{}'.format(MAJOR, MINOR, REVISION)

    @property
    def version(self):
        return '{}.{}.{}'.format(self.MAJOR, self.MINOR, self.REVISION)

    @classmethod
    def cls_version(cls):
        return '{}.{}.{}'.format(cls.MAJOR, cls.MINOR, cls.REVISION)

    @staticmethod
    def static_version():
        return '{}.{}.{}'.format(Language.MAJOR, Language.MINOR, Language.REVISION)


l = Language()
print(l.version)
print(Language.cls_version())
print(Language.static_version())

line_break()

def full_version():
    return '{}.{}.{}'.format(Language.MAJOR, Language.MINOR, Language.REVISION)

print(full_version())

line_break()

class Language:
    MAJOR = 3
    MINOR = 7
    REVISION = 4

    @classmethod
    def cls_version(cls):
        return '{}.{}.{}'.format(MAJOR, MINOR, REVISION)

#print(Language.cls_version())

line_break()

MAJOR = 0
MINOR = 0
REVISION = 1

print(Language.cls_version())

line_break()

MAJOR = 0
MINOR = 0
REVISION = 1

def gen_class():
    MAJOR = 0
    MINOR = 4
    REVISION = 2

    class Language:
        MAJOR = 3
        MINOR = 7
        REVISION = 4

        @classmethod
        def version(cls):
            return '{}.{}.{}'.format(MAJOR, MINOR, REVISION)

    return Language


cls = gen_class()

print(cls.version())

line_break()

import inspect

print(inspect.getclosurevars(cls.version))



line_break()

name = 'Guido'

class MyClass:
    name = 'Raymond'
    list_1 = [name] * 3
    list_2 = [name.upper() for i in range(3)]

    @classmethod
    def hello(cls):
        return '{} says hello'.format(name)


print(MyClass.list_1)
print(MyClass.hello())
print(MyClass.list_2)