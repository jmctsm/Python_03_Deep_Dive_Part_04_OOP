from math import pi
import urllib
import urllib.request
from time import perf_counter

def line_break():
    x = 0
    while x < 20:
        print("*", end="")
        x += 1
    print("\n")


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        print("Calculating area...")
        return pi * (self.radius ** 2)

c = Circle(1)
print(c.area)

c.radius = 2
print(c.area)
print(c.area)
print(c.area)

line_break()

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self._area = None

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        # if radius value is set we invalidate our cached _area value
        # we could make thie more intelligent and see if the radius has actually changed
        # but keeping it simple
        self._area = None
        # we could even add validation here, like value has to be numeric, non-negative, etc
        self._radius = value

    @property
    def area(self):
        if self._area is None:
            # value not cached - calculate it
            print("Calculating area ...")
            self._area = pi * (self._radius ** 2)
        return self._area

c = Circle(1)
print(c.area)
print(c.area)
print(c.area)
print(c.area)
c.radius = 2
print(c.area)
print(c.area)
print(c.area)
print(c.area)

line_break()


class WebPage:
    def __init__(self, url):
        self.url = url
        self._page = None
        self._load_time_secs = None
        self._page_size = None

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value
        self._page = None
        # We'll lazy load the page - i.e. we wait until some property is requested

    @property
    def page_size(self):
        if self._page is None:
            # need to first download the page
            self.download_page()
        return self._page_size

    @property
    def time_elapsed(self):
        if self._page is None:
            self.download_page()
        return self._load_time_secs

    def download_page(self):
        self._page_size = None
        self._load_time_secs = None
        start_time = perf_counter()
        with urllib.request.urlopen(self.url) as f:
            self._page = f.read()
        end_time = perf_counter()

        self._page_size = len(self._page)
        self._load_time_secs = end_time - start_time

urls = [
    'https://www.google.com',
    'https://www.python.org',
    'https://www.yahoo.com'
]

for url in urls:
    page = WebPage(url)
    print(f'{url} \tsize={format(page.page_size, "_")} \telapsed={page.time_elapsed:.2f} secs')