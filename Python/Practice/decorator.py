from time import time

def timer(func):
    def wrapper():
        start = time()
        func()
        end = time()
        print(f"Duration: {end-start}")
    return wrapper

@timer
def sum_nums():
    result = 0
    for x in range(1000000):
        result += x

sum_nums()