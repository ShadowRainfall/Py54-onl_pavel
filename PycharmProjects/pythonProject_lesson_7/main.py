import time

def guard_zero(operate):
    def inner(x, y):
        if y == 0:
            print('error')
            quit()
        return operate(x, y)
    return inner

@guard_zero
def divide(x, y):
    return x / y

def meassure_time(func):
    def transl(count):
        s = time.time()
        func()
        e = time.time()
        count = e - s
        print(f'Processing time for {func}: [ {count} ]')
        return count
    return transl

@meassure_time
def time_count():
    time.sleep(2)

def upper_case(func):
    def wrapper(word):
        modify = word.upper()
        return func(modify)
    return wrapper

@meassure_time
@upper_case
def greeting(word):
    return print(word)

tup_1 = (divide(4, 1), time_count(divide(4, 1)))
tup_2 = (greeting, time_count(divide(4, 1)))
print(f'Result tuple 1 {tup_1}')
print(f'Result tuple 2 {tup_2}')