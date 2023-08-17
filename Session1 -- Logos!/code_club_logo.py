'''
Make a logo for code club.

Created by: Benjamin Metha
Last Updated: Aug 03, 2023
'''

import matplotlib.pyplot as plt
import numpy as np

C = np.array([
[1,1,1,1,1],
[1,0,0,0,0],
[1,0,0,0,0],
[1,0,0,0,0],
[1,1,1,1,1]
])

flag = np.zeros((9,9))

flag[1:6,1:6]  += 2*C

flag[3:8, 3:8] += C

plt.imshow(flag)
plt.show()


# Let's get weirder 

from scipy.ndimage import gaussian_filter

bigC = np.array([
[1,1,1,1,1,1,1,1,1],
[1,0,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0,0],
[1,1,1,1,1,1,1,1,1]
])

big_flag = np.zeros((21,21))

flag[5:14, 5:14] += bigC

flag[9:18, 9:18] += bigC

new_flag = gaussian_filter(big_flag,1)

plt.imshow(new_flag)

