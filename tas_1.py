import math
def multipliers(number):
    if number == 1:
        print(1)
    lst = []
    i = 2
    while number != 1:
        if number % i == 0:
            number = number // i
            lst.append(i)
            continue
        i+=1
    print(lst)


def equation(a, b, c):
    d = b*b - 4*a*c
    if d >= 0:
        sd = math.sqrt(d)
        s = lambda k: format((-b+k*sd)/(2*a))
        l = ' and '.join(set(map(s, (-1,1))))
    print 'Otvet: %s' % l

def simple(number):
    for i in range(2, number - 1):
        if not number % i:
            return False
        else:
            return True

# atm uses only 100, 50, 20, 10, 5 and 1 notes.
def atm(summ):
    a = summ % 100
    b = summ / 100
    a1 = a % 50
    c = a / 50
    a2 = a1 % 20
    d = a1 / 20
    a3 = a2 % 10
    e = a2 / 10
    a4 = a3 % 5
    f = a3 / 5
    a5 = a4 % 1
    g = a4 / 1
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)
    print(g)


print multipliers(30030)

print equation(2, 19, 35) # 2x^2 + 19x + 3
# 5 = 0

print simple(13)

print atm(287)