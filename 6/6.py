import numpy as np

n = 100
sol = (np.arange(1,n+1).sum())**2 - np.array([i**2 for i in np.arange(1,n+1)]).sum()
print(sol)