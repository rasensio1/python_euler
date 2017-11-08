import cProfile
from python_euler import test_func


def true_first():
    a = [True] + [False] * 10000
    any(a)

def true_last():
    b = [False] * 10000 + [True]
    any(b)

cProfile.run("test_func(true_first, 1000)") 
cProfile.run("test_func(true_last, 1000)") 
