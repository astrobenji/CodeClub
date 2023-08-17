'''
In: Data file full of galaxies from MERAXES: their IDs, x,y,z coordinates, and 
radii

Out: How many galaxies are contained by each bubble?
'''


import numpy as np
from astropy.io import ascii
from sklearn.metrics.pairwise import euclidean_distances 

REDSHIFT = 10

def read_data():
	'''
	Open Manu's data file.
	
	Parameters
	---------
	
	Returns
	-------
	
	the data file, opened and cleaned
	'''
	tab = ascii.read('../Data/GalMeraxes.dat')
	return tab
	

if __name__ == '__main__':
	tab = read_data()
	x = tab['col2']
	y = tab['col3']
	z = tab['col4']
	r = tab['col5'] * (1+REDSHIFT) # converting physical to comoving parsecs
	
	# stack coordinates together
	coords = np.vstack([x,y,z]).T
	
	# Find all distances between all galaxies
	dist_matrix = euclidean_distances(coords, coords)
	