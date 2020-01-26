"""
measure.py
molssi workshop: A python package for analyzing and visualizing xyz file.

Handles the calculations like bonds and angles
"""

import numpy as np
from .atom_data import atomic_weights

def calculate_distance(r_A, r_B):
    """
    Calculate the distance between two points given as numpy arrays.
    
    Parameters
    ----------
    r_A, r_B : np.ndarray
        The coordinates of points A and B.
        
    Returns
    -------
    distance : float
        The distance between the two points A and B.
        
    Examples
    --------
    >>> r1 = np.array([1, 0, 0])
    >>> r2 = np.array([3, 0, 0])
    >>> calculate_distance(r1, r2)
    2.0
    """
    
    if not isinstance(r_A, np.ndarray) or not isinstance(r_B, np.ndarray):
        raise TypeError("Input must be of type np.ndarray for calculate_distance function!!!")
    
    distance_vector = (r_A - r_B)
    distance = np.linalg.norm(distance_vector)
    return distance

def calculate_angle(r_A, r_B, r_C, degrees=False):
    # Calculate the angle between three points. Answer is given in radians by default, but can be given in degrees
    # by setting degrees=True
    AB = r_B - r_A
    BC = r_B - r_C
    theta = np.arccos(np.dot(AB, BC)/(np.linalg.norm(AB)*np.linalg.norm(BC)))

    if degrees:
        return np.degrees(theta)
    else:
        return theta
def calculate_molecular_mass(symbols):
    """Calculate the mass of a molecule.
   
    Parameters
    ----------
    symbols : list
       A list of elements.
   
    Returns
    -------
    mass : float
       The mass of the molecule
    """
     
    mass = 0
    for i in range(len(symbols)):
        mass = mass + atomic_weights[symbols[i]]
    return mass

def calculate_center_of_mass(symbols, coordinates):
    """Calculate the center of mass of a molecule.
   
    The center of mass is weighted by each atom's weight.
   
    Parameters
    ----------
    symbols : list
       A list of elements for the molecule
    coordinates : np.ndarray
       The coordinates of the molecule.
   
    Returns
    -------
    center_of_mass: np.ndarray
       The center of mass of the molecule.
    Notes
    -----
    The center of mass is calculated with the formula
   
    .. math:: \\vec{R}=\\frac{1}{M} \\sum_{i=1}^{n} m_{i}\\vec{r_{}i}
   
    """

    total_mass = calculate_molecular_mass(symbols)
   
    mass_array = np.zeros([len(symbols), 1])
   
    for i in range(len(symbols)):
        mass_array[i] = atomic_weights[symbols[i]]
   
    center_of_mass = sum(coordinates * mass_array) / total_mass
   
    return center_of_mass