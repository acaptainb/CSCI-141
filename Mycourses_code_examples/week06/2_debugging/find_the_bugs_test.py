from find_the_bugs import *

def test_exponent():
    assert(raise_exponent(2, 3) == 8)
def test_add():
    assert(add(2, 3) == 5)
def test_sub():
    assert(sub(2, 3) == -1)
def test_mul():
    assert(mul(2, 3) == 6)
def test_div():
    assert(div(3, 2) == 1.5)
def test_floor_div():
    assert(floor_div(3, 2) == 1)
def test_modulo():
    assert(modulo(11, 5) == 1)