'''
goal: testing whether timeit() may return different value everytime

result ==> true
'''

from timeit import timeit

def loop(n=0):
    for i in range(n):
        print('hi')

print(f"time = {timeit(lambda: loop(3), number=1)}")