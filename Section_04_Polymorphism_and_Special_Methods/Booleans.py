def line_break():
    x = 0
    print("\n\n")
    while x < 20:
        print("*", end="")
        x += 1
    print("\n\n")


line_break()


class Person:
    pass


p = Person()
print(bool(p))

line_break()


class MyList:
    def __init__(self, length):
        print('__init__ called')
        self._length = length

    def __len__(self):
        print('__len__ called')
        return self._length

l1 = MyList(0) # so __len__ will return 0
l2 = MyList(10) # so __len__ will return 10
print(bool(l1))
print(bool(l2))

line_break()


class MyList:
    def __init__(self, length):
        print('__init__ called...')
        self._length = length

    def __len__(self):
        print('__len__ called...')
        return self._length

    def __bool__(self):
        print('__bool__ called...')
        return self._length > 0

p1 = MyList(0)
p2 = MyList(100)
print(bool(p1))
print(bool(p2))

line_break()


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = Point(0, 0)
p2 = Point(1, 1)

print(bool(p1), bool(p2))

line_break()


class Point:
    def __init__(self, x, y):
        print('__init__ called...')
        self.x = x
        self.y = y

    def __bool__(self):
        print('__bool__ called...')
        return self.x != 0 or self.y != 0


p1 = Point(0, 0)
p2 = Point(1, 1)

print(bool(p1), bool(p2))
print(bool(p1.x or p1.y))
print(bool(p2.x or p2.y))

line_break()


class Point:
    def __init__(self, x, y):
        print('__init__ called...')
        self.x = x
        self.y = y

    def __bool__(self):
        print('__bool__ called...')
        return self.x or self.y


p1 = Point(0, 0)
p2 = Point(1, 1)

print(bool(p1.__bool__()), bool(p2.__bool__()))
try:
    print(bool(p1))
except TypeError as ex:
    print(ex)

line_break()


class Point:
    def __init__(self, x, y):
        print('__init__ called...')
        self.x = x
        self.y = y

    def __bool__(self):
        print('__bool__ called...')
        return bool(self.x or self.y)


p1 = Point(0, 0)
p2 = Point(1, 1)
print(bool(p1), bool(p2))
