#!/usr/bin/env python

import numpy as np
from sklearn.neighbors import KDTree

gals = np.loadtxt('GalMeraxes.dat')
gals[:, -1] *= 11 # Correct physical bubble radii to comoving

print("Building KDTree...")
tree = KDTree(gals[:, 1:-1], leaf_size=5)
print("done.")

bubble_gals = np.where(gals[:, -1] != 0)[0]
print(bubble_gals)
with open("gal_counts.dat", "w") as f:
    for gal_idx in bubble_gals:
        id = gals[gal_idx, 0]
        print(f"Doing galaxy id {int(id)}")
        pos = gals[gal_idx, 1:-1].reshape(1,-1)
        radius = gals[gal_idx, -1]
        gal_count = tree.query_radius(pos, r=radius, count_only=True)
        print(f"{int(id)} {gal_count[0]}", file=f)
