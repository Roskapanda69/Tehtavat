#Tehtävä 1 viiko 3

from matplotlib import pyplot as plt, patches
import numpy as np
from fractions import Fraction as fr

import matplotlib as mpl

fig = plt.figure()
ax = fig.subplots()

ymp = patches.Circle((0, 0), radius=1, fill=0)
ax.add_patch(ymp)

# Move left y-axis and bottom x-axis to centre, passing through (0,0)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

# Eliminate upper and right axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Show ticks in the left and lower axes only
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.axis('equal')

plt.xticks([-1, 0, 1], minor=True)
plt.yticks([-1, 0, 1])

pii=np.pi
pist_xy=np.array([ pii, pii, pii, pii, 2*pii, 3*pii, 5*pii, pii, 3*pii, 2*pii ])
nim=np.array([ 6, 4, 3, 2, 3, 4, 6, 1, 2, 1 ])
varit=np.array(['red', 'green', 'blue', 'orange', 'red', 'green', 'blue', 'orange', 'red', 'green' ])

text=[r'30 deg', r'45 deg', r'60 deg', r'90' , r'120 deg' , r'135 deg', r'150 deg', r'180 deg', r'270 deg', r'360 deg' ]

x = np.cos(pist_xy/nim)
y = np.sin(pist_xy/nim)

plt.scatter(x, y, color=varit, marker='X')

for i in range(len(pist_xy)):
    plt.annotate(text[i],
             xy=(np.cos(pist_xy[i]/nim[i]), np.sin(pist_xy[i]/nim[i])), xycoords='data',
             xytext=(+30, +5), textcoords='offset points', fontsize=12,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0"))


plt.show()