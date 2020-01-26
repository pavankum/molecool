"""
Unit tests for measure
"""

# Import package, test suite, and other packages as needed
import numpy as np
import molecool 
import pytest

def test_calculate_distance():
    """Sample test to check calculate_distance is working """
    
    r1 = np.array([1, 0, 0])    
    r2 = np.array([3, 0, 0])

    expected_distance = 2

    calculated_distance = molecool.calculate_distance(r1, r2)

    assert calculated_distance == expected_distance    

def test_calculate_distance_typeerror():


    r1 = [1, 0, 0]
    r2 = [2, 0, 0]
    with pytest.raises(TypeError):
        calculated_distance = molecool.calculate_distance(r1, r2)

    
def test_calculate_angle():
    """Sample test to check calculate_anlge is working"""
    
    r1 = np.array([1, 0, 0])
    r2 = np.array([0, 0, 0])
    r3 = np.array([0, 1, 0])
    
    expected_angle = 90
    calculated_angle = molecool.calculate_angle(r1, r2, r3, degrees=True)
    
    assert calculated_angle == expected_angle
	
@pytest.mark.parametrize("p1, p2, p3, expected_angle", [
    (np.array([np.sqrt(2)/2, np.sqrt(2)/2, 0]), np.array([0, 0, 0]), np.array([1, 0 , 0]), 45),
    (np.array([0, 0, -1]), np.array([0, 1, 0]), np.array([1, 0, 0]), 60),
])
def test_calculate_angle_many(p1, p2, p3, expected_angle):
    calculated_angle = molecool.calculate_angle(p1, p2, p3, degrees=True)
	
    assert pytest.approx(calculated_angle) == expected_angle

def test_molecular_mass():
    symbols = ['C', 'H', 'H', 'H', 'H']
    
    calculated_mass = molecool.calculate_molecular_mass(symbols)

    actual_mass = molecool.atom_data.atomic_weights['C'] + molecool.atom_data.atomic_weights['H'] +\
         molecool.atom_data.atomic_weights['H'] + molecool.atom_data.atomic_weights['H'] + molecool.atom_data.atomic_weights['H']
    
    assert actual_mass == calculated_mass