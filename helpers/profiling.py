def test_func(func, n, args=None):
    for _ in xrange(n):
        if args:
            func(args)
        else:
            func()

