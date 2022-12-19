import matplotlib.pyplot as plt
import numpy as np

#linspace
#start, stop
a = np.linspace(0, 8)
b = np.exp(-a)
plt.plot(a,b)
plt.show()
print(a)
print(len(a))
print(b)