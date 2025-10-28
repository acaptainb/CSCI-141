from collatz_steps import collatz_steps_tail as cs

def test_collatz_steps_10():
    # setup
    n = 10
    expected = 7
    # invoke
    actual = cs(n)
    # analyze
    assert actual == expected

def test_collatz_steps():
    # setup
    n = [1, 2, 10, 13, 21]
    expected = [1, 2, 7, 10, 8]
    for i in range(len(n)):
        # invoke
        actual = cs(n[i])
        # analyze
        assert actual == expected[i]
