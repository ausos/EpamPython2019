import functools
import time

########
# HW 1
########

# problem9
print('Problem 9: ',
      [(a * b * (a**2 + b**2)**(0.5)) for a in range(1, 500)
       for b in range(1, 500) if a+b+(a**2+b**2)**(0.5) == 1000][0])

# problem6
print('Problem 6: ',
      sum(i for i in range(101))**2 - sum(i**2 for i in range(101)))

# problem48
print('Problem 48: ', sum(i**i for i in range(1, 1001)) % 10000000000)

# problem40


def problem_40(positions: list):

    numbers = str().join(str(i) for i in range(0, positions[-1]))

    return functools.reduce(lambda x, y: int(x)*int(y),
                            [numbers[i] for i in positions])

print('Problem 40: ', problem_40([1, 10, 100, 1000, 10000, 100000, 1000000]))

########
# HW 2
########


def is_armstrong(number):

    return number == sum(map(lambda x: int(x)**int(len(str(number))),
                         str(number)))

assert is_armstrong(153) is True, 'Число Армстронга'
assert is_armstrong(10) is False, 'Не число Армстронга'


########
# HW 3
########

def collatz_steps(n):

    step = 0
    if n != 1 and n != 0:
        while n != 1:
            n = n/2 if n % 2 == 0 else n * 3 + 1
            step += 1
    else:
        return 0

    return step

assert collatz_steps(16) == 4
assert collatz_steps(12) == 9
assert collatz_steps(1000000) == 152

########
# HW 4
########


def applydecorator(decorator):

    def new_decorator(f):

        def wrapper(*args, **kwargs):

            return decorator(f, *args, **kwargs)

        return wrapper

    return new_decorator


@applydecorator
def saymyname(f, *args, **kwargs):
    print('Name is', f.__name__)
    return f(*args, **kwargs)


@saymyname
def foo(*whatever):
    return whatever

print(*(foo(40, 2)))

########
# HW 5
########


def profiling_decorator(func):
    start = time.time()

    def wrapper(*args, **kwargs):

        global counter
        counter[0] += 1

        return func(*args, **kwargs)

    counter[1] = time.time() - start

    return wrapper

counter = [int(), float()]


@profiling_decorator
def fib(n):
    if n < 2:
        return n

    return fib(n-1) + fib(n-2)

print(fib(30), counter)

counter = [int(), float()]


@profiling_decorator
def fib2(n):
    fib1 = fib2 = 1
    i = 2
    while i < n:
        fib_sum = fib2 + fib1
        fib1 = fib2
        fib2 = fib_sum
        i += 1

    return fib_sum

print(fib2(30), counter)

counter = [int(), float()]


@profiling_decorator
def fib3(n):
    a = 0
    b = 1
    for __ in range(n):
        a, b = b, a + b

    return a
print(fib3(30), counter)