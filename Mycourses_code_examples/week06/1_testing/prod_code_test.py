import prod_code

def test_add_1_2():
    # setup
    a = 1
    b = 2
    expected = 3
    # invoke
    actual = prod_code.add_nums(a, b)
    # analyze
    assert actual == expected

def test_add_5_6():
    # setup
    a = 5
    b = 6
    expected = 11
    # invoke
    actual = prod_code.add_nums(a, b)
    # analyze
    assert actual == expected

def test_collatz_1():
    # setup
    n = 1
    expected = 1
    # invoke
    actual = prod_code.collatz(n)
    # analyze
    assert actual == expected

def test_collatz_2():
    # setup
    n = 2
    expected = 1
    # invoke
    actual = prod_code.collatz(n)
    # analyze
    assert actual == expected

def test_collatz_5():
    # setup
    n = 5
    expected = 1
    # invoke
    actual = prod_code.collatz(n)
    # analyze
    assert actual == expected

def test_collatz_loop():
    # setup
    a = 1
    b = 500
    expected = 1
    # invoke
    for n in range(a, b):
        actual = prod_code.collatz(n)
        # analyze
        assert actual == expected

def test_collatz_steps_1():
    # setup
    n = 1
    expected = 1
    # invoke
    actual = prod_code.collatz_steps(n)
    # analyze
    assert actual == expected

def test_collatz_steps_2():
    # setup
    n = 2
    expected = 2
    # invoke
    actual = prod_code.collatz_steps(n)
    # analyze
    assert actual == expected

def test_collatz_steps_10():
    # setup
    n = 10
    expected = 7
    # invoke
    actual = prod_code.collatz_steps(n)
    # analyze
    assert actual == expected

def test_collatz_steps_21():
    # setup
    n = 21
    expected = 8
    # invoke
    actual = prod_code.collatz_steps(n)
    # analyze
    assert actual == expected

def test_collatz_steps_13():
    # setup
    n = 13
    expected = 10
    # invoke
    actual = prod_code.collatz_steps(n)
    # analyze
    assert actual == expected