def line_break():
    x = 0
    print("\n\n")
    while x < 20:
        print("*", end="")
        x += 1
    print("\n\n")


line_break()

print(f"type(Exception) = {type(Exception)}")
ex = Exception()

print(f"ex.__class__ , type(ex) = {ex.__class__ , type(ex)}")

print(f"isinstance(ex, BaseException) = {isinstance(ex, BaseException)}")

print(f"issubclass(IndexError, LookupError) = {issubclass(IndexError, LookupError)}")

print(f"issubclass(LookupError, Exception) = {issubclass(LookupError, Exception)}")

l = [1, 2, 3]
# print(f"l[4] = {l[4]}")
try:
    print(f"l[4] = {l[4]}")
except IndexError as ex:
    print(f"ex.__class__ : str(ex) = {ex.__class__} : {str(ex)}")
try:
    print(f"l[4] = {l[4]}")
except LookupError as ex:
    print(f"ex.__class__ : str(ex) = {ex.__class__} : {str(ex)}")

try:
    print(f"l[4] = {l[4]}")
except Exception as ex:
    print(f"ex.__class__ : str(ex) = {ex.__class__} : {str(ex)}")

line_break()

ex = ValueError("custom message")

print(f"str(ex) = {str(ex)}")
print(f"repr(ex) = {repr(ex)}")

line_break()


def func_1():
    func_2()


def func_2():
    func_3()


def func_3():
    # Create an instance of a ValueError exception, and raise it
    raise ValueError()


# func_3()
# func_1()


def func_2():
    try:
        func_3()
    except ValueError:
        print("error occurred - silencing it")


func_1()

line_break()


def square(seq, index):
    return seq[index] ** 2


def squares(seq, max_n):
    for i in range(max_n):
        yield square(seq, i)


l = [1, 2, 3]

# print(f"list(squares(1, 4)) = {list(squares(l, 4))}")


def square(seq, index):
    return seq[index] ** 2


def squares(seq, max_n):
    for i in range(max_n):
        try:
            yield square(seq, i)
        except Exception:
            return


l = [1, 2, 3]

print(f"list(squares(1, 5)) = {list(squares(l, 5))}")

# print(f"'a' ** 2 = {'a' ** 2}")


def square(seq, index):
    return seq[index] ** 2


def squares(seq, max_n):
    for i in range(max_n):
        try:
            yield square(seq, i)
        except IndexError:
            return


l = [1, 2, "3", 4, 5]

# print(f"list(squares(1, 10)) = {list(squares(l, 10))}")
l = [1, 2, 3]
print(f"list(squares(1, 10)) = {list(squares(l, 10))}")

line_break()

try:
    print(1 / 0)
except:
    print("Exception occurred")
