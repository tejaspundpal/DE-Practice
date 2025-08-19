def fib():
    for cur in (0,1):
        last = cur
        yield cur
    while True:
        yield cur
        last,cur = cur,last + cur

f = fib()

for i in range(0,10):
    print(next(f))