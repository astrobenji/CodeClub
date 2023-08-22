'''
stamp_resizer.py
'''

from astropy.io import fits
import numpy as np

WANTED_SIZE = 50 # pixels

def open_data():
	return fits.open('../Data/BoRG_sources.fits')
	
def resize_hdu(hdu_in, new_size):
	'''
	Parameters
	----------
	hdu_in: a hdu object
	
	new_size: int
		Size to bin image to.
	
	Returns
	-------
	resized_hdu: a hdu object with shape (50, 50)
	'''
	header = hdu_in.header
	data   = hdu_in.data
	
	new_header           = header.copy()
	new_header['NAXIS1'] = new_size
	new_header['NAXIS2'] = new_size
	
	new_data = np.zeros(new_shape)
	
	
	# Step 1: bin to be just below wanted_size
	
	# because images are square (i checked them all) only need 1 ratio:
	bin_factor = int(header['NAXIS1'] / new_header['NAXIS1']  + 0.999)
	n_after_binning = header['NAXIS1'] / bin_factor
	
	binned_data  = np.zeros((n_after_binning, n_after_binning))
	for jj in range(n_after_binning):
		for ii in range(n_after_binning):
			binned_data[ii, jj]  = np.sum(data[bin_factor*ii: bin_factor*(ii+1), 
								               bin_factor*jj: bin_factor*(jj+1)])
	
	# Step 2: add whitespace
	
	
	
	
if __name__ == '__main__':
	hdu_list = open_data()
	# Everything but the first file is an ImageHDU
	n_images = len(hdu_list - 1)
	resized_hdu_list = []
	# Keep primary HDU
	resized_hdu_list.append(hdu_list[0])
	# Resize each HDU; add to list
	for ii in range(n_images):
		new_hdu = resize_hdu(hdu_list[ii+1], (WANTED_SIZE, WANTED_SIZE))
		resized_hdu_list.append(new_hdu)
	# Save output	
	output_hdu_list = fits.HDUList(resized_hdu_list)
	output_hdu_list.writeto('../Outputs/BoRG_Sources_{0}x{0}.fits'.format(WANTED_SIZE))