"""
functions.py
molssi workshop: A python package for analyzing and visualizing xyz file.

Handles the calculations like bonds and angles
"""
import os
import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

def calculate_distance(rA, rB):
    # This function calculates the distance between two points given as numpy arrays.
    d=(rA-rB)
    dist=np.linalg.norm(d)
    return dist

def calculate_angle(rA, rB, rC, degrees=False):
    # Calculate the angle between three points. Answer is given in radians by default, but can be given in degrees
    # by setting degrees=True
    AB = rB - rA
    BC = rB - rC
    theta=np.arccos(np.dot(AB, BC)/(np.linalg.norm(AB)*np.linalg.norm(BC)))

    if degrees:
        return np.degrees(theta)
    else:
        return theta

def build_bond_list(coordinates, max_bond=1.5, min_bond=0):
    
    # Find the bonds in a molecule (set of coordinates) based on distance criteria.
    bonds = {}
    num_atoms = len(coordinates)

    for atom1 in range(num_atoms):
        for atom2 in range(atom1, num_atoms):
            distance = calculate_distance(coordinates[atom1], coordinates[atom2])
            if distance > min_bond and distance < max_bond:
                bonds[(atom1, atom2)] = distance

    return bonds

