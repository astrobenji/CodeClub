#!/usr/bin/env python

from astropy.io import fits
import matplotlib.pyplot as plt
from scipy.ndimage import zoom
from skimage.measure import block_reduce
import numpy as np

TARGET_SIZE = 50

f = fits.open("BoRG_sources.fits")
for image in f:
    if image.data is None:
        continue
    data = image.data 
    factor = data.shape[0]/TARGET_SIZE
    if factor > 1: # Image is bigger than target size
        new = zoom(data, 1/factor)
        fig, (ax1, ax2) = plt.subplots(2) 
        print(f"Old size: {data.shape[0]}")
        print(f"New size: {new.shape[0]}")
        ax1.imshow(data)
        ax2.imshow(new)
        plt.show()
    else: # Pad with zeros UNFINISHED
        axis = data.shape[0]
        extra = TARGET_SIZE - axis

        new = np.zeros((TARGET_SIZE, TARGET_SIZE))

