def line_break():
    x = 0
    print("\n\n")
    while x < 20:
        print("*", end="")
        x += 1
    print("\n\n")

class Person:
    def hello(arg='default'):
        print(f'Hello, with arg = {arg}')


print(Person.hello())
print(Person.hello)
p = Person()
print(p.hello)
p.hello()
print(hex(id(p)))

line_break()

class MyClass:
    def hello():
        # This is an instance method, we just forgot to add a parameter to capture the instance
        # when this is called from an instance - to this will fail
        print('Hello...')

    def instance_hello(arg):
        print(f'Hello from {arg}')

    @classmethod
    def class_hello(arg):
        print(f'Hello from {arg}')


m = MyClass()
MyClass.hello()
try:
    m.hello()
except TypeError as ex:
    print(ex)
m.instance_hello()
try:
    MyClass.instance_hello()
except TypeError as ex:
    print(ex)

print(MyClass.class_hello)
print(m.class_hello)
print(MyClass.instance_hello)
print(m.instance_hello)
MyClass.class_hello()
m.class_hello()

line_break()

class MyClass:
    def instance_hello(self):
        print(f'Instance method bound to {self}')

    @classmethod
    def class_hello(cls):
        print(f'Class method bound to {cls}')

    @staticmethod
    def static_hello():
        print('Static method not bound to anything')


m = MyClass()
m.instance_hello()
MyClass.class_hello()
m.class_hello()
print(MyClass.static_hello)
print(m.static_hello)
MyClass.static_hello()
m.static_hello()

line_break()

from datetime import datetime, timezone, timedelta

class Timer:
    tz = timezone.utc # class variable to store the timezone - default to UTC

    @classmethod
    def set_tz(cls, offset, name):
        cls.tz = timezone(timedelta(hours=offset), name)


Timer.set_tz(-7, 'MST')
print(Timer.tz)
t1 = Timer()
t2 = Timer()
print(t1.tz, t2.tz)
Timer.set_tz(-8, 'PST')
print(t1.tz, t2.tz)

line_break()

class Timer:
    tz = timezone.utc # class variable to store the timezone - default to UTC

    @staticmethod
    def current_dt_utc():
        return datetime.now(timezone.utc)

    @classmethod
    def set_tz(cls, offset, name):
        cls.tz = timezone(timedelta(hours=offset), name)


print(Timer.current_dt_utc())
t = Timer()
print(t.current_dt_utc())

line_break()

class Timer:
    tz = timezone.utc # class variable to store the timezone - default to UTC

    @staticmethod
    def current_dt_utc():
        return datetime.now(timezone.utc)

    @classmethod
    def set_tz(cls, offset, name):
        cls.tz = timezone(timedelta(hours=offset), name)

    @classmethod
    def current_dt(cls):
        return datetime.now(cls.tz)


print(Timer.current_dt_utc(), Timer.current_dt())
t1 = Timer()
t2 = Timer()
print(t1.current_dt_utc(), t1.current_dt())
print(t2.current_dt())
t2.set_tz(-7, "MST")
print(Timer.__dict__)
print(Timer.current_dt_utc(), Timer.current_dt())
print(t1.current_dt(), t2.current_dt())

line_break()

class TimerError(Exception):
    """ A custom exception used for Timer Class"""
    # since """...""" is a statement, we don't need a pass

class Timer:
    tz = timezone.utc # class variable to store the timezone - default to UTC

    def __init__(self):
        # use these instance variables to keep track of start/end times
        self._time_start = None
        self._time_end = None

    @staticmethod
    def current_dt_utc():
        """ REturns non-naive current UTC"""
        return datetime.now(timezone.utc)

    @classmethod
    def set_tz(cls, offset, name):
        cls.tz = timezone(timedelta(hours=offset), name)

    @classmethod
    def current_dt(cls):
        return datetime.now(cls.tz)

    def start(self):
        # internally we always non-naive UTC
        self._time_start = self.current_dt_utc()
        self._time_end = None

    def stop(self):
        if self._time_start is None:
            # cannot stop if Timer was not started!
            raise TimerError("Timer must be started before it can be stopped.")
        self._time_end = self.current_dt_utc()

    @property
    def start_time(self):
        if self._time_start is None:
            raise TimerError("Timer has not been started")
        # since tz is a class variable, we can just as easily access it from self
        return self._time_start.astimezone(self.tz)

    @property
    def end_time(self):
        if self._time_end is None:
            raise TimerError("Timer has not been stopped")
        # since tz is a class variable, we can just as easily access it from self
        return self._time_end.astimezone(self.tz)

    @property
    def elapsed(self):
        if self._time_start is None:
            raise TimerError('Timer must be started before an elapsed time is available')
        if self._time_end is None:
            # time has not been stopped, calculate between start and now
            elapsed_time = self.current_dt_utc() - self._time_start
        else:
            # timer has been stopped, calculate elapsed between start and end
            elapsed_time = self._time_end - self._time_start

        return elapsed_time.total_seconds()


from time import sleep
t1 = Timer()
t1.start()
sleep(2)
t1.stop()
print(f'Start time: {t1.start_time}')
print(f'End time: {t1.end_time}')
print(f'Elapsed: {t1.elapsed} seconds')


t2 = Timer()
t2.start()
sleep(5)
t2.stop()
print(f'Start time: {t2.start_time}')
print(f'End time: {t2.end_time}')
print(f'Elapsed: {t2.elapsed} seconds')

line_break()

Timer.set_tz(-7, 'CST')
t1 = Timer()
t1.start()
sleep(2)
t1.stop()
print(f'Start time: {t1.start_time}')
print(f'End time: {t1.end_time}')
print(f'Elapsed: {t1.elapsed} seconds')


t2 = Timer()
t2.start()
sleep(5)
t2.stop()
print(f'Start time: {t2.start_time}')
print(f'End time: {t2.end_time}')
print(f'Elapsed: {t2.elapsed} seconds')

