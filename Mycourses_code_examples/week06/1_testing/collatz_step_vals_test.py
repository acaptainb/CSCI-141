from collatz_step_vals import *

def test_collatz_step_vals_10():
    # setup
    n = 10
    expected = "10,5,16,8,4,2,1"
    # invoke
    actual = collatz_step_vals(n)
    # analyze
    assert actual == expected

def test_collatz_step_vals_13():
    # setup
    n = 13
    expected = "13,40,20,10,5,16,8,4,2,1"
    # invoke
    actual = collatz_step_vals(n)
    # analyze
    assert actual == expected
