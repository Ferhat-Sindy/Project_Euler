import numpy as np

fib = [1,2] 
answer = 2

while fib[-1] < 4e6:
    fib.append(fib[-1]+fib[-2])
    if fib[-1]%2 ==0:
        answer += fib[-1]

print(answer)