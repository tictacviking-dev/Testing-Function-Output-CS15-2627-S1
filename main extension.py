import pytest

def square(num):
    result = num * num
    return result

def avg(a, b):
    total = a + b
    avg = total / 2
    return avg

def c_to_f(c):
    f = (c * 9/5) + 32
    return f


def test_square1():
    assert square(3) == 9

def test_square2():
    assert square(-4) == 16

def test_avg1():
    assert avg(4, 6) == 5

def test_avg2():
    assert pytest.approx(avg(0.1, 0.2)) == 0.15

def test_c_to_f1():
    assert c_to_f(0) == 32

def test_c_to_f2():
    assert c_to_f(100) == 212