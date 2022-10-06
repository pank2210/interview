import sys
from datetime import datetime as dt

dict = {}

def fibonacci_number0(n):
    if n <= 1:
        return n
    return fibonacci_number(n - 1) + fibonacci_number(n - 2)

def fibonacci_number(n):
    if n <= 1:
        return n
    if n not in dict:
      dict[n] = fibonacci_number(n - 1) + fibonacci_number(n - 2)
      return dict[n]
    else:
      return dict[n]

if __name__ == '__main__':
    #input_n = int(input())
    input_n = int(sys.argv[1])
    t0 = dt.now()
    print(fibonacci_number0(input_n))
    print("time taken - ",dt.now()-t0)
    t0 = dt.now()
    print(fibonacci_number(input_n))
    print("time taken - ",dt.now()-t0)
