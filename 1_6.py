import time
from itertools import *
import random
import os

def it_list_one():
    list = sorted([10, 2, 37, 4, 54])
    print [x for x in list]
    print [x for x in enumerate("abcd")]
it_list_one()

def it_list_two(list):
    if len(list) < 5:
        print [x for x in enumerate(list)]
    else:
        print sorted(list)
list_2 = ['one', 'four', 'abc', 'three']
it_list_two(list_2)

def it_list_three(list_one, list_two):
    for i in chain(iter(list_one), iter(list_two)):
        print i,
    print ' '
it_list_three([1, 3, 5], [2, 4, 6])

def gen_list_one():
    list = [x**3 for x in range(3, 47, 2)]
    yield list
gen_list_one()

def gen_list_two():
    list = [x**3 for x in range(3, 47, 2) if x % 3 != 0]
    yield list
gen_list_two()

def gen_list_three():
    list_one = [x**2 for x in range(2, 50, 2)]
    list_two = [x**3 for x in range(3, 57, 2)]
    for i in list_one:
        yield i
    for s in list_two:
        yield s
gen_list_three()

def iter_test():
    for i in takewhile(lambda x: x < 0, [9, -7, 7, -8]):
        print i,
    for i in dropwhile(lambda x: x < 0, [9, -7, 7, -8]):
        print i,
    print ' '
    for i in count(1):
        print i,
        if i > 30:
            break
    print ' '
    for i in chain(iter([1, 3, 5]), iter([2, 4, 6])):
        print i,
    print ' '
    print islice([(2, 5, 3, 2, 10, 3)], 0, 3)

iter_test()

def func(a):
    print a**2 / 2
    print a / 2 * 2
func(4)

def generator():
    a = 10 ** 2 * random.randrange(5, 20, 2)
    b = 10 ** 2 * random.randrange(5, 20, 2)
    c = 10 ** 2 * random.randrange(5, 20, 2)
    d = 10 ** 2 * random.randrange(5, 20, 2)
    list = {'One': a,
            'Two': b,
            'Three': c,
            'Four': d}
    print list
generator()

print (lambda x, y: x ** y)(134684, 2)

def function_one(a, b):
    result = a ** b
    def function_two(result):
        if result < 50:
            res = result * 10
            print res
        else:
            print result
    function_two(result)

function_one(40, 6)
def timer(f):
    def tmp(*args, **kwargs):
        t = time.time()
        res = f(*args, **kwargs)
        print "Time: %f" % (time.time()-t)
        return res

    return tmp

@timer
def func(x, y):
    return x + y

func(1, 2)

def decor(f):
    print 'Function name is "Function"'
@decor
def func():
    a = 10 ** 2
    print a


a = 40
def decorator_two(a):
    try:
        function_two(a)
    except:
        print 'Too big number'

@decorator_two
def function_two(a):
    if a < 50:
        print True
    else:
        f = 'Too big number'