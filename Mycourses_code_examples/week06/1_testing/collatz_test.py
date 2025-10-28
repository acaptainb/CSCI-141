from collatz import *

def test_collatz_1():
    # setup
    exp = 1
    n = 1
    # invoke
    actual = collatz(n)
    #analyze
    assert exp == actual

def test_collatz_2():
    # setup
    exp = 1
    n = 2
    # invoke
    actual = collatz(n)
    #analyze
    assert exp == actual

def test_collatz_3():
    # setup
    exp = 1
    n = 3
    # invoke
    actual = collatz(n)
    #analyze
    assert exp == actual

def test_collatz_4_10():
    # setup
    exp = 1
    for n in range(4,11):
        # invoke
        actual = collatz(n)
        #analyze
        assert exp == actual
