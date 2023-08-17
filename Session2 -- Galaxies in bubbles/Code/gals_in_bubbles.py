'''
In: Data file full of galaxies from MERAXES: their IDs, x,y,z coordinates, and 
radii

Out: How many galaxies are contained by each bubble?
'''


import numpy as np
from sklearn.pairwise import euclidean_distances


if __name__ == '__main__':
	df = read_data()
	