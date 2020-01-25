"""
pdb.py

module for manipulating pdb format files
"""

import numpy as np

def open_pdb(file_location):
    """
	This function reads in a atomic coordinates file in protein database (pdb) format and returns the atom names and coordinates.
	
	Parameters
	----------
	file_location: string
		directory of the file location along with the filename to read
		
	Returns
	-------
	symbols: string
		atomic symbols
	coordinates: np.ndarray
		atomic [x, y, z] coordinates
		
	Examples
	--------
	>>> open_pdb(oxygen.pdb)
	O 0.0 0.0 0.0
	
	"""
	
    with open(file_location) as f:
        data = f.readlines()
        
    coordinates = []
    symbols = []
    
    for line in data:
        if 'ATOM' in line[0:6] or 'HETATM' in line[0:6]:
            symbols.append(line[76:79].strip())
            atom_coordinates = [float(x) for x in line[30:55].split()]
            coordinates.append(atom_coordinates)
    
    # Convert list to numpy array
    coordinates = np.array(coordinates)
    
    return symbols, coordinates
