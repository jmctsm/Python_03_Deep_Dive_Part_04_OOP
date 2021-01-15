def line_break():
    x = 0
    print("\n\n")
    while x < 20:
        print("*", end="")
        x += 1
    print("\n\n")

line_break()

from datetime import datetime

class TimeUTC:
    def __get__(self, instance, owner_class):
        print(f'__get__ called, self={self}, instance={instance}, owner_class={owner_class}')
        return datetime.utcnow().isoformat()

class Logger1:
    current_time = TimeUTC()

class Logger2:
    current_time = TimeUTC()

print(f'Logger1.current_time = {Logger1.current_time}')
print(f'Logger2.current_time = {Logger2.current_time}')

l1 = Logger1()
print(f'hex(id(l1)) = {hex(id(l1))}')
print(f'l1.current_time = {l1.current_time}')

l2 = Logger2()
print(f'hex(id(l2)) = {hex(id(l2))}')
print(f'l2.current_time = {l2.current_time}')

line_break()

from datetime import datetime

class TimeUTC:
    def __get__(self, instance, owner_class):
        if instance is None:
            ''' called from class '''
            return self
        else:
            ''' called from instance '''
            return datetime.utcnow().isoformat()

class Logger:
    current_time = TimeUTC()

print(f'Logger.current_time = {Logger.current_time}')
l = Logger()
print(f'l.current_time = {l.current_time}')

line_break()
class Logger:
    @property
    def current_time(self):
        return datetime.utcnow().isoformat()

print(f'Logger.current_time = {Logger.current_time}')
l = Logger()
print(f'l.current_time = {l.current_time}')

line_break()

class TimeUTC:
    def __get__(self, instance, owner_class):
        if instance is None:
            ''' called from class '''
            return self
        else:
            ''' called from instance '''
            print(f'__get__ called in {self}')
            return datetime.utcnow().isoformat()

class Logger:
    current_time = TimeUTC()

l1 = Logger()
l2 = Logger()

print(f'l1.current_time , l2.current_time = {l1.current_time} , {l2.current_time}')

line_break()

class Countdown:
    def __init__(self, start):
        self.start = start + 1

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            self.start -= 1
            return self.start

class Rocket:
    countdown = Countdown(10)

rocket1 = Rocket()
rocket2 = Rocket()

print(f'rocket1.countdown = {rocket1.countdown}')
print(f'rocket2.countdown = {rocket2.countdown}')
print(f'rocket1.countdown = {rocket1.countdown}')

line_break()

class IntegerValue:
    def __set__(self, instance, value):
        print(f'__set__ called, instance={instance}, value={value}')

    def __get__(self, instance, owner_class):
        if instance is None:
            print('__get__ called from class')
        else:
            print(f'__get__ called, instance={instance}, owner_class={owner_class}')

class Point2D:
    x = IntegerValue()
    y = IntegerValue()

print(f'Point2D.x = {Point2D.x}')

p = Point2D()
print(f'p.x = {p.x}')
p.x = 100

line_break()

class IntegerValue:
    def __set__(self, instance, value):
        print(f'__set__ called, instance={instance}, value={value}')
        self._value = int(value)

    def __get__(self, instance, owner_class):
        if instance is None:
            print('__get__ called from class')
            return self
        else:
            print(f'__get__ called, instance={instance}, owner_class={owner_class}')
            return self._value

class Point2D:
    x = IntegerValue()
    y = IntegerValue()

p1 = Point2D()

p1.x = 1.1
p1.y = 2.2

print(f'p1.x , p1.y = {p1.x} , {p1.y}')

p2 = Point2D()
print(f'p2.x , p2.y = {p2.x} , {p2.y}')
p2.x = 100.9
print(f'p1.x , p2.x = {p1.x} , {p2.x}')
