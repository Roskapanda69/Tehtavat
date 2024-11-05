from cProfile import label
from math import radians

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import legend

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C,S = np.cos(X), np.sin(X)

plt.figure (figsize=(13,9))

plt.xlabel('X-akselit jotain')
plt.ylabel('Y-akselit jotain')
pii=np.pi
plt.yticks([1, 0.75, 0.50, 0.25, 0.00 , -0.25, -0.50, -0.75, -1],
           ['π' ,'π /4','π/2','π/6','0','-π/6','π/2','-π/4','-π'])

plt.plot(X,C, color='orange', linestyle=':', label= 'Cos',)
plt.plot(X,S, color='purple', linestyle=':', label= 'Sin',)
legend()



plt.show()