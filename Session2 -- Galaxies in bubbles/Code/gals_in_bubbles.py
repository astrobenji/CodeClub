'''
In: Data file full of galaxies from MERAXES: their IDs, x,y,z coordinates, and 
radii

Out: How many galaxies are contained by each bubble?
'''


import numpy as np
from sklearn.metrics.pairwise import euclidean_distances 

REDSHIFT = 10

def read_data(n_rows = None):
	'''
	Open Manu's data file.
	
	Parameters
	---------
	n_rows: only return the first n_rows
	
	Returns
	-------
	
	the data file, opened and cleaned
	'''
	tab = ascii.read('../Data/GalMeraxes.dat')
	if n_rows is None:
		return tab
	else:
		return tab[:n_rows]

if __name__ == '__main__':
	tab = read_data())
	x = tab['col2']
	y = tab['col3']
	z = tab['col4']
	r = tab['col5'] * (1+REDSHIFT) # converting physical to comoving parsecs
	
	# stack all coordinates together
	all_coords = np.vstack([x,y,z]).T
	
	n_gals = len(x)
	n_in_bubble = np.empty(n_gals)
	for ii in range(n_gals):
		gal_coords = np.array(x[ii], y[ii], z[ii])
		# Find all distances between all galaxies
		dist_to_gal = euclidean_distances(gal_coords, all_coords)
	
		n_in_bubble[ii] = np.sum(dist_to_gal < r[ii])
	