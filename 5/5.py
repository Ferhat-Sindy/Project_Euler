from math import factorial
import numpy as np

flag = True

i = 9699690

while flag:
    if (np.mod(i,np.arange(1,21)) == np.zeros(20)).all():
        break
    if i == 10000000:
        break
    i+=1

print(i)