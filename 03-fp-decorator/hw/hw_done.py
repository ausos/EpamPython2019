import functools
import time

########
# HW 1
########

# problem9
[(a * b * (a**2 + b**2)**(0.5)) for a in range(1, 500) for b in range(1, 500) if a+b+(a**2+b**2)**(0.5) == 1000][0]

# problem6
sum(i for i in range(101))**2 - sum(i**2 for i in range(101))

# problem48
sum(i**i for i in range(1, 1001)) % 10000000000

# problem40


def problem_40(positions: list):

    numbers = str().join(str(i) for i in range(0, positions[-1]))

    return functools.reduce(lambda x, y: int(x)*int(y), [numbers[i] for i in positions])

problem_40([1, 10, 100, 1000, 10000, 100000, 1000000])

########
# HW 2
########


def is_armstrong(number):

    return number == sum(map(lambda x: int(x)**int(len(str(number))), str(number)))

assert is_armstrong(153) == True, 'Число Армстронга'
assert is_armstrong(10) == False, 'Не число Армстронга'


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


def make_cache(seconds=10):

    def decorator(func):

        storage = {}

        @functools.wraps(func)
        def inner(*args, **kwargs):
            keys = (*args, *kwargs.items())
            if keys not in storage or storage[keys][0] + seconds <= time.time():
                storage[keys] = (time.time(), func(*args, **kwargs))
            return storage[keys][1]

        return inner

    return decorator


@make_cache()
def fib(n):
    if n < 2:
        return n

    return fib(n-1) + fib(n-2)

fib(100)
