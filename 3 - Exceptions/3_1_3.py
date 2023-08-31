# StopIteration
def stop_iteration_error():
    y = []
    x = iter(y)
    return (x.__next__())


# ValueError
def value_error():
    l = []
    l.remove(0)


# ZeroDivisionError
def zero_division_error():
    return 1 / 0


# AssertionError
def assertion_error():
    x = 1
    y = 0
    assert y != 0
    return (x + y)

# ImportError


def import_error():
    from srgdrsg import eagrsdtrh

# KeyError


def key_error():
    d = {1: 'a', 2: 'b'}
    return d[0]


# SyntaxError למשל חסר פסיקים וכדומה


# IndentationError טעויות הזחה

# TypeError
def type_error():
    return 1 + b
