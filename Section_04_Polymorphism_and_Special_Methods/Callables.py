def line_break():
    x = 0
    print("\n\n")
    while x < 20:
        print("*", end="")
        x += 1
    print("\n\n")


from time import perf_counter
from functools import wraps
from functools import partial
from collections import defaultdict
from time import sleep
import random

line_break()

class Person:
    def __call__(self):
        print('__call__ called>>>')
        
p = Person()
print(type(p))
p()

line_break()


def my_func(a, b, c):
    return a, b, c
    
partial_func = partial(my_func, 10, 20)

print(type(partial))
print(type(my_func))
print(type(partial_func))
print(partial_func(30))

line_break()

def my_func(a, b, c):
    return a, b, c

class Partial:
    def __init__(self, func, *args):
        self._func = func
        self._args = args
        
    def __call__(self, *args):
        return self._func(*self._args, *args)
        
partial_func = Partial(my_func, 10, 20)
print(type(partial_func))

print(partial_func(30))

print(callable(print))

print(callable(partial))

print(callable(partial_func))

class Person:
    def __init__(self, name):
        self.name = name
        
print(callable(Person))

p = Person('Alex')

print(callable(p))


line_break()

# Example: Cache with a cache-miss counter


def default_value():
    return 'N/A'
    
d = defaultdict(default_value)

print(d['a'])

print(d.items())

line_break()

miss_counter = 0

def default_value():
    global miss_counter
    miss_counter += 1
    return 'N/A'
    
d = defaultdict(default_value)

d['a'] = 1
print(d['a'])
print(d['b'])
print(d['c'])
print(d['d'])

print(miss_counter)

del miss_counter

d = defaultdict(default_value)

try:
    print(d['a'])
except NameError as ex:
    print(ex)
    
line_break()

class DefaultValue:
    def __init__(self):
        self.counter = 0
        
    def __iadd__(self, other):
        if isinstance(other, int):
            self.counter += other
            return self
        raise ValueError('Can only increment with an integer value.')
        
default_value_1 = DefaultValue()

default_value_1 += 1

print(default_value_1.counter)

line_break()

class DefaultValue:
    def __init__(self):
        self.counter = 0
        
    def __iadd__(self, other):
        if isinstance(other, int):
            self.counter += other
            return self
        raise ValueError('Can only increment with an integer value.')
        
    def __call__(self):
        self.counter += 1
        return 'N/A'
        
def_1 = DefaultValue()
def_2 = DefaultValue()

cache_1 = defaultdict(def_1)
cache_2 = defaultdict(def_2)

print(cache_1['a'], cache_1['b'])
print(def_1.counter)
print(cache_2['a'])
print(def_2.counter)


line_break()

class DefaultValue:
    def __init__(self, default_value):
        self.default_value = default_value
        self.counter = 0
        
    def __iadd__(self, other):
        if isinstance(other, int):
            self.counter += other
            return self
        raise ValueError('Can only increment with an integer value.')
        
    def __call__(self):
        self.counter += 1
        return self.default_value

cache_def_1 = DefaultValue(None)
cache_def_2 = DefaultValue(0)

cache_1 = defaultdict(cache_def_1)
cache_2 = defaultdict(cache_def_2)

print(cache_1['a'], cache_1['b'], cache_1['a'])
print(cache_def_1.counter)

print(cache_2['a'], cache_2['b'], cache_2['c'])
print(cache_def_2.counter)

line_break()

# Profiling Functions

def profiler(fn):
    counter = 0
    total_elapsed = 0
    avg_time = 0

    @wraps(fn)
    def inner(*args, **kwargs):
        nonlocal counter
        nonlocal total_elapsed
        nonlocal avg_time
        counter += 1
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        total_elapsed += (end - start)
        avg_time = total_elapsed / counter
        return result

    # we need to give a way to our users to look at the
    # counter and avg_time values - spoiler: this won't work
    inner.counter = counter
    inner.avg_time = avg_time
    return inner


random.seed(0)

@profiler
def func1():
    sleep(random.random())

print(func1(), func1())

print(func1.counter)

line_break()

def profiler(fn):
    _counter = 0
    _total_elapsed = 0
    _avg_time = 0

    @wraps(fn)
    def inner(*args, **kwargs):
        nonlocal _counter
        nonlocal _total_elapsed
        nonlocal _avg_time
        _counter += 1
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        _total_elapsed += (end - start)
        return result

    # we need to give a way to our users to look at the
    # counter and avg_time values - but we need to make sure
    # it is using a cell reference!
    def counter():
        # this will now be a closure with a cell pointing to _counter
        return _counter

    def avg_time():
        return _total_elapsed / _counter

    inner.counter = counter
    inner.avg_time = avg_time
    return inner

@profiler
def func1():
    sleep(random.random())

print(func1(), func1())

print(func1.counter())

print(func1.avg_time())

line_break()

class Profiler:
    def __init__(self, fn):
        self.counter = 0
        self.total_elapsed = 0
        self.fn = fn

    def __call__(self, *args, **kwargs):
        self.counter += 1
        start = perf_counter()
        result = self.fn(*args, **kwargs)
        end = perf_counter()
        self.total_elapsed += (end - start)
        return result

    @property
    def avg_time(self):
        return self.total_elapsed / self.counter

@Profiler
def func_1(a, b):
    sleep(random.random())
    return (a, b)

print(func_1(1, 2))

print(func_1.counter)

print(func_1(2, 3))

print(func_1.counter)

print(func_1.avg_time)

@Profiler
def func_2():
    sleep(random.random())

print(func_2(), func_2(), func_2())
print(func_2.counter, func_2.avg_time)

