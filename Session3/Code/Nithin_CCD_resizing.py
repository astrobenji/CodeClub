'''
Resizing Stamps
This program opens a fits file of stamps and resizes all of them to 50x50
I've added some parts to time it and to plot the stamps, but that's moreso 
because I was curious and I like plotting things, the actual challenge was
just resizing the stamp

- Nithin Babu
'''

import numpy as np
import matplotlib.pyplot as plt

from astropy.io import fits
from astropy.table import Table
from astropy.visualization import ZScaleInterval

import time as t

# This function shrinks the stamps
def shrink_stamp(data, newshape):
    '''
    Resizes an AxA array to a BxB array
    This particular function just picks particular pixels 
    as a representative of a group of pixels, So it may not 
    work for every case.
    '''
    # Confirm the dimensions are the same shape
    assert len(data.shape) == len(newshape)

    # This defines the slices of the image we're going to take
    arr = np.linspace(0,data.shape[0],newshape[0]+1, dtype=int)[:-1]
    coords = np.tile(arr,(newshape[0],1))
    
    # Return the shrunken image
    return data[tuple([coords.transpose(),coords])]

# Open up the fits file and get the two images and catalogue
with fits.open("BoRG_sources.fits") as f:
    # For the times
    times = np.zeros(len(f)-1)
    sizes = np.zeros(len(f)-1)

    # To store the new stamps
    new_stamps = []
    
    # loop through all the sources and create 50x50 stamps
    for i in range(1,len(f)):
        start_time = t.time()
        # Get the postage stamp (original size)
        original_stamp = f[i].data
        size = original_stamp.shape[0]
        sizes[i-1] = size**2
        
        # If the postage stamp is too big, shrink it
        if size > 50:
            stamp = shrink_stamp(original_stamp,(50,50))
    
        # If the postage stamp is too small, put some white space
        elif size < 50:
            stamp = np.zeros((50,50))
            margin_b = int((50 - size) / 2)
            margin_e = int(margin_b + size)
            stamp[margin_b:margin_e, margin_b:margin_e] = original_stamp

        new_stamps.append(stamp)

        times[i-1] = t.time() - start_time
        
        # # I like plotting things, but its not needed for this purpose
            
        # # This is just for consistent colour and clarity
        # z = ZScaleInterval()
        # zmin, zmax = z.get_limits(f[1].data)

        # # Plot the new stamp
        # fig = plt.figure(figsize=(3,3))
        # plt.imshow(stamp, cmap="gray", vmin=zmin, vmax=zmax, origin="lower")
        # plt.title(f[i].name)
        # plt.show()

    fig = plt.figure(figsize=(10,10))
    plt.scatter(sizes, times)
    plt.title("Stamp Creation times")
    plt.xlabel("Source size (px^2)")
    plt.ylabel("Time (s)")
    plt.show()

'''
If you wanna check other options, I'd suggest looking at skimage.transform.resize,
and Scipy's Rebinning Cookbook (https://scipy-cookbook.readthedocs.io/items/Rebinning.html)
My function is actually a modified version of theirs.
'''
