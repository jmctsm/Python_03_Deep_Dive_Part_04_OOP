def line_break():
    x = 0
    print("\n\n")
    while x < 20:
        print("*", end="")
        x += 1
    print("\n\n")

line_break()

class Location:
    __slots__ = 'name', '_longitude', '_latitude'

    def __init__(self, name, longitude, latitude):
        self._longitude = longitude
        self._latitude = latitude
        self.name = name

    @property
    def longitude(self):
        return self._longitude

    def latitude(self):
        return self._latitude

print(f'Location.__dict__ = {Location.__dict__}')
Location.map_service = 'Google Maps'
print(f'Location.__dict__ = {Location.__dict__}')
l = Location('Mumbai', 19.0760, 72.8777)
print(f'l.name, l.longitude, l.latitude = {l.name}, {l.longitude}, {l.latitude()}')

try:
    print(f'l.__dict__ = {l.__dict__}')
except AttributeError as ex:
    print(ex)

try:
    l.map_link = 'https://maps.google.com/...'
except AttributeError as ex:
    print(ex)
del l.name
try:
    print(f'l.name = {l.name}')
except AttributeError as ex:
    print(f'Attribute Error: {ex}')

l.name = 'Mumbai'
print(f'l.name = {l.name}')
