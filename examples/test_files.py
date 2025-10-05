import test
def test_add_one_4():
    #setup
    x=4
    expecter = 16
    #invoke
    actual = test.square(x)
    #analyze
    assert actual == expecter


def test_add_one_1():
    # setup
    x = 1
    expecter = 1
    # invoke
    actual = test.collatz(x)
    # analyze
    assert actual == expecter

def test_add_one_2():
    # setup
    x = 2
    expecter = 1
    # invoke
    actual = test.collatz(x)
    # analyze
    assert actual == expecter
def test_collatz_7():
    # setup
    x = 7
    expecter = 10
    # invoke
    actual = test.collatz2(x )
    # analyze
    assert actual == expecter
