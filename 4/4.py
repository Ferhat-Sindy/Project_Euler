import numpy as np

def is_palindrone(i):
    i_np = np.array(list(str(i)))
    return (np.flip(i_np) == i_np).all()

threedigits = np.arange(100,1000)

sol_set = np.array(np.sort([j*k for j in threedigits for k in threedigits]))

for l in reversed(sol_set):
    if is_palindrone(l):
        break

print(l)
